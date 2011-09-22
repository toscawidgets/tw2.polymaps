""" Samples of how to use tw2.polymaps

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PolyMap, PollingPolyMap
from resources import custom_css_1, custom_css_2
from geojsonify import geojsonify
from tw2.core import JSSymbol

import random

class DemoPolyMap(PolyMap):
    data_url = '/polymap_demo/'

    interact = True

    # You should get your own one of these at http://cloudmade.com/register
    cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"

    # To style the map tiles
    cloudmade_tileset = 'midnight-commander'

    # Both specify the css_class AND include your own custom css file that
    # specifies what it looks like.
    css_class = 'sample-tw2-polymaps-container-1'
    def prepare(self):
        super(DemoPolyMap, self).prepare()
        self.resources.append(custom_css_1)

    properties_callback = """function (_layer) {
        _layer.on("load", org.polymaps.stylist()
        .title(function(d) { return "Lon/lat:  " + d.properties.ATTR }));
        return _layer
    }"""

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
                    geometry=geojson.Point([mod(lon), mod(lat)]),
                    properties={'ATTR': "%s, %s" % (mod(lon), mod(lat))},
                ) for i in range(n)

            ]
        )
        return json


import tw2.core as twc
mw = twc.core.request_local()['middleware']
mw.controllers.register(DemoPolyMap, 'polymap_demo')

class DemoPollingPolyMap(PollingPolyMap):
    data_url = '/polymap_polling_demo/'
    interval = 1000
    layer_lifetime = 1500

    # You should get your own one of these at http://cloudmade.com/register
    cloudmade_api_key = "1a1b06b230af4efdbb989ea99e9841af"

    # To style the map tiles
    cloudmade_tileset = 'pale-dawn'

    # Both specify the css_class AND include your own custom css file that
    # specifies what it looks like.
    css_class = 'sample-tw2-polymaps-container-2'
    def prepare(self):
        super(DemoPollingPolyMap, self).prepare()
        self.resources.append(custom_css_2)

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

mw.controllers.register(DemoPolyMap, 'polymap_polling_demo')
