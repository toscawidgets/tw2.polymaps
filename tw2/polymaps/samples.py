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

    def prepare(self):
        super(DemoPolyMap, self).prepare()
        self.resources.append(custom_css)

    @classmethod
    @geojsonify
    def request(cls, req):
        import geojson
        # Bay Area:
        lat = 37.775
        lon = -122.4183333

        json = geojson.FeatureCollection(
            features=[
                geojson.Feature(
                    geometry=geojson.Point([lon, lat])
                )
            ]
        )
        return json


import tw2.core as twc
mw = twc.core.request_local()['middleware']
mw.controllers.register(DemoPolyMap, 'polymap_demo')
