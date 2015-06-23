# -*- coding: utf-8 -*-
import json

import django
from django.http import HttpResponse
from django.template.response import TemplateResponse


def json_view(request):
    data = json.dumps({"some": "data"})

    # note: mimetype renamed to content_type in django1.5
    if django.VERSION < (1, 5):
        response_kwargs = {'mimetype': 'application/json'}
    else:
        response_kwargs = {'content_type': 'application/json'}

    return HttpResponse(data, **response_kwargs)


def text_view(request):
    return HttpResponse("some data")


def templated_view(request):
    return TemplateResponse(request, 'templated.html')
