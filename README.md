[![Build Status](https://travis-ci.org/swistakm/ddt-envelope.svg)](https://travis-ci.org/swistakm/ddt-envelope)
[![Coverage Status](https://coveralls.io/repos/swistakm/ddt-envelope/badge.svg)](https://coveralls.io/r/swistakm/ddt-envelope)

# ddt-envelope

Simple solution to use django-debug-toolbar with non HTML views. Helps 
in inspecting/profiling endpoints that do not return HTML responses 
(like JSON endpoint).

It is tested on latest point releases of: `django1.4`, `django1.5`, `django1.6`,
`django1.7`, `django1.8` and each python version that is supported by given
django releases accordingly (ie. `python2.6`, `python2.7`, `python3.2`,
`python3.3`, `python3.4`).

# Instalation

0. Install with pip:

    ```
    pip install ddt-envelope
    ```

0. Add `ddt-envelope` to your `INSTALLED_APPS`:

    ```python
   
    if DEBUG is True:
        INSTALLED_APPS += (
            'ddt_envelope',
        )
    ```
  
3. Add `ddt_envelope` at the end of your `urls.py`

    ```python
    from django.conf import settings
    
    if 'ddt_envelope' in settings.INSTALLED_APPS:
       urlpatterns += patterns('',
           # note: you can use any prefix other than '__ddte__' but make
           #       sure it does not conflict with other url patterns
           url(r'^__ddte__/', include('ddt_envelope.urls')),
       )
    ```

# Usage

Once installed and configured just insert `__ddte__` or your custom prefix 
after hostname in browser of choice to inspect non-html views like:

```
http://example.com/__ddte__/maybe/json/
```

# Customizing output

You can customize `ddt_envelope` responses either by providing custom
template name for `ddt_envelope.views.EnvelopeView` or by overriding
`ddte/envelope.html` template. Context variables passed to this templeta are:

* `path` - "real" path of inspected view
* `response` - response object returned by target inspected view
* `headers` - dictionary of headers available in response returned by target 
  inspected view
* `content` - string with raw response content (JSON it will be reformated
  using `json.dumps(..., indent=4)`)
