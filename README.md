============
ddt-envelope
============

Simple solution to use django-debug-toolbar with non HTML views. Helps in e.g. profiling RESTful APIs.


Instalation
===========

#. Add the debug_toolbar directory to your Python path.

#. Add `ddt-envelope` to your `INSTALLED_APPS`:

   ```
   INSTALLED_APPS = (
       ...
       'ddt_envelope',
   )
   ```
#. Add `ddt_envelope` to your `urls.py`

   ```
   urlpatterns = patterns('',
       ...
       url(r'^__ddte__/', include('ddt_envelope.urls')),
   )
   ```

Using ddt-envelope
==================

To inspect non-html view with ddt-envelope just insert `__ddte__` after hostname, e.g.:

```
http://example.com/__ddte__/maybe/json/
```
