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

    TEST_WEBSETTING = 'default value'
    SPAM = 'default spam'

Then you can get setting values from websettings.

.. code-block:: python

    >>> from websettings import websettings
    >>> websettings.TEST_WEBSETTING
    'default value'

After you set overriding value (like 'after value') by using
web interface...:

.. code-block:: python

    >>> websettings.TEST_WEBSETTING
    'after value'

Install
=======

This library is registered in PyPI as ``django-websettings``.
You can install it as much as you like.

Setting
=======

Websettings file
----------------

The position of the setting file is specified by a WEBSETTINGS_MODULE
in your project's settings.py file:

.. code-block:: python

    # In your settings.py file.
    WEBSETTING_MODULE = 'yourproject.websettings'

Under project directory seems good.
You should put these setting key's by UPPER_CASE.

Web interface URL
-----------------

The url to web interface to set setting values can be included like this:

.. code-block:: python

    # In your urls.py file.
    url(r'^websettings/', include('websettings.urls'))

The admin user can only access this page.

Backend
-------

django-websettings is designed to correspond to multiple backend
to store settings.

You can specify the back end module to set a WEBSETTINGS_BACKEND
in your project's setting.py file:

.. code-block:: python

    # In your settings.py file
    WEBSETTINGS_BACKEND = 'path.to.backend_module'

A DB backend (websetting.backends.db) is used by default.

Testing
=======

django-websettings is tested by some environments,
check out the `Travis CI report
<https://travis-ci.org/hirokiky/django-websettings>`_.
