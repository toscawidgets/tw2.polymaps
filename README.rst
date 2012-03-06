tw2.polymaps
=================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _polymaps: http://polymaps.org/

tw2.polymaps is a `toscawidgets2 (tw2)`_ wrapper for `polymaps`_.

Live Demo
---------

Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.polymaps>`_.

Links
-----

You can `get the source from github <http://github.com/toscawidgets/tw2.polymaps>`_,
check out `the PyPI page <http://pypi.python.org/pypi/tw2.polymaps>`_, and
report or look into `bugs <http://github.com/toscawidgets/tw2.polymaps/issues/>`_.

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`polymaps`_ is a JavaScript library for image- and vector-tiled maps using SVG.

This module, tw2.polymaps, provides `toscawidgets2 (tw2)`_ widgets that render `polymaps`_ maps!

Sampling tw2.polymaps in the WidgetBrowser
------------------------------------------

The best way to scope out ``tw2.polymaps`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.polymaps/tw2/polymaps/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.polymaps.git
    $ cd tw2.polymaps
    $ mkvirtualenv tw2.polymaps
    (tw2.polymaps) $ pip install tw2.devtools
    (tw2.polymaps) $ python setup.py develop
    (tw2.polymaps) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
