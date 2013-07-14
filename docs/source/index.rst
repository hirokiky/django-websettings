.. django-websettings documentation master file, created by
   sphinx-quickstart on Sun Jul 14 13:06:17 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

django-websettings
===================

Django application to provide a web interface
to set a yet another django's settings.

If you want to learm about django-websettings,
please read :doc:`introduction of django-websettings <intro>` first.

Resources
---------

- `Docs <https://django-websettings.readthedocs.org/en/latest/>`_
- `PyPI <https://pypi.python.org/pypi/django-websettings>`_
- `Code <https://github.com/hirokiky/django-websettings>`_
- `Testing <https://travis-ci.org/hirokiky/django-websettings>`_

At a glance
------------

Setting values:

.. code-block:: python

    # In websettings.py file
    HTTP_DRUM_PLAYER = 'Ritsu Tainaka'
    HTTP_BASS_PLAYER = 'Mio Akiyama'

Getting setting values:

.. code-block:: python

    >>> from websettings import websettings
    >>> websettings.HTT_BASS_PLAYER
    'Mio Akiyama'

On web interface:

.. image:: _static/list_view.jpg
   :alt: list view of django-websettings

Changed the value:

.. image:: _static/edit_view.jpg
   :alt: edit view of django-websettings

And then:

.. code-block:: python

    >>> from websettings import websettings
    >>> websettings.HTT_BASS_PLAYER
    'Jun Suzuki'

That's it!
You like this and want to learn more, please read
:doc:`introduction of django-websettings <intro>` first.

Contents
--------

.. toctree::
   :maxdepth: 2

   intro
   advanced
