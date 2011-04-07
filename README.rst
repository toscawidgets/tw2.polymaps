tw2.polymaps
=================

:Author: Ralph Bean <ralph.bean@gmail.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _polymaps: http://polymaps.org/

tw2.polymaps is a `toscawidgets2 (tw2)`_ wrapper for `polymaps`_.

Live Demo
---------

Peep the `live demonstration <http://craftsman.rc.rit.edu/module?module=tw2.polymaps>`_.

Links
-----

You can `get the source from github <http://github.com/ralphbean/tw2.polymaps>`_,
check out `the PyPI page <http://pypi.python.org/pypi/tw2.polymaps>`_, and
report or look into `bugs <http://github.com/ralphbean/tw2.polymaps/issues/>`_.

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
-------------------------------------

The best way to scope out ``tw2.polymaps`` is to load its widgets in the 
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.polymaps/samples.py``

To give it a try you'll need git, mercurial, python, and virtualenv.  Run:

    ``git clone git://github.com/ralphbean/tw2.polymaps.git``

    ``cd tw2.polymaps``

The following script will set up all the necessary tw2 dependencies in a
python virtualenv:

    ``./develop-tw2-destroy-and-setup.sh``

The following will enter the virtualenv and start up ``paster tw2.browser``:

    ``./develop-tw2-start.sh``

...and browse to http://localhost:8000/ to check it out.



