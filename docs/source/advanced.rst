Advanced
========

Printing correct value of websettings
-------------------------------------

You can check the current value of settings by using
``print_websettings`` management command:

.. code-block:: sh

   $ python manage.py print_websettings
   HTT_DRUM_PLAYER                          = 'Ritsu Tainaka'
   HTT_BASS_PLAYER                          = 'Mio Akiyama'

Also you can use these keyword arguments:

- format:

  - json: printing result as json.
  - simple: printing result as simple format like assignment of python.

- indent: accept a number to specify indent size (only available as json format)

Deleting trash values
---------------------

There is an anxiety leaving trash data on backend:

.. code-block:: python

    >>> from websettigs import websettings
    >>> websettings.clear_trash()

Writing own backend
-------------------

django-websettings is designed to correspond to multiple backend
to store settings.

This guide explain the way to write your own backend and use it.

Interface guide for backend
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A backend is a just one module contains three functions.

- getsetting(key): a function to get the setting value by `key`.
- setsetting(key, value): a function to set `value` correspond to `key`.
- exclude_clear(keys): a function to clear setting values exclude `keys`.

When fail getting or setting the values,
the function should raise AttributeError.

Using your backend
^^^^^^^^^^^^^^^^^^^

You can specify the back end module to set a WEBSETTINGS_BACKEND
in your project's setting.py file:

.. code-block:: python

    # In your settings.py file
    WEBSETTINGS_BACKEND = 'path.to.backend_module'

A DB backend (websetting.backends.db) is used by default.
