# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns

import views

urlpatterns = patterns('ddt_envelope.views',
    url(r'^(?P<next>.+)$', views.EnvelopeView.as_view(), name='ddte'),
)