""" Samples of how to use tw2.polymaps

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PolyMap
from resources import custom_css
from geojsonify import geojsonify
from tw2.core import JSSymbol

import random

class js(JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)

class DemoPolyMap(PolyMap):
    css_class = 'tw2-polymaps-container'

    data_url = '/polymap_demo/'
    interact = True

    def prepare(self):
        super(DemoPolyMap, self).prepare()
        self.resources.append(custom_css)

    @classmethod
    @geojsonify
    def request(cls, req):
        import geojson

        n = 40
        lat, lon = 37.775, -122.4183333
        mod = lambda x : x + random.random() * 0.05 - 0.025

        json = geojson.FeatureCollection(
            features=[
                geojson.Feature(
                    geometry=geojson.Point([mod(lon), mod(lat)])
                ) for i in range(n)

            ]
        )
        return json


import tw2.core as twc
mw = twc.core.request_local()['middleware']
mw.controllers.register(DemoPolyMap, 'polymap_demo')
