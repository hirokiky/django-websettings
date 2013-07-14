==================
django-websettings
==================

.. image:: https://travis-ci.org/hirokiky/django-websettings.png
   :target: https://travis-ci.org/hirokiky/django-websettings

Django application to provide a web interface
to set a yet another django's settings.

Basic usage
===========

You can set a setting file containing some key-value pairs
like django's settings.py.
Then a web interface to set setting values will be provided automatically.

The value in the setting file is handled as default value of web interface.
A new value set from web interface overrides that default value.

The setting file will be like this:

.. code-block:: python

    HTT_DRUM_PLAYER = 'Ritsu Tainaka'
    HTT_BASS_PLAYER = 'Mio Akiyama'

Then you can get setting values from websettings.

.. code-block:: python

    >>> from websettings import websettings
    >>> websettings.HTT_BASS_PLAYER
    'Mio Akiyama'

After you set overriding value (like 'Jun Suzuki') by using
web interface...:

.. code-block:: python

    >>> websettings.TEST_WEBSETTING
    'Jun Suzuki'

Resources
=========

- `Docs <https://django-websettings.readthedocs.org/en/latest/>`_
- `PyPI <https://pypi.python.org/pypi/django-websettings>`_
- `Code <https://github.com/hirokiky/django-websettings>`_
- `Testing <https://travis-ci.org/hirokiky/django-websettings>`_
