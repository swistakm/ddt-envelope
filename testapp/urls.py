# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from . import views


urlpatterns = patterns(
    '',
    url(r'^json/$', views.json_view),
    url(r'^text/$', views.text_view),
    url(r'^templated/$', views.templated_view),

    url(r'^__ddte__/', include('ddt_envelope.urls')),
)
