""" Samples of how to use tw2.polymaps

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PolyMap
from resources import custom_css
from tw2.core import JSSymbol

import random

class js(JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)

class DemoPolyMap(PolyMap):
    css_class = 'tw2-polymaps-container'

    def prepare(self):
        super(DemoPolyMap, self).prepare()
        self.resources.append(custom_css)

