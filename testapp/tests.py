# -*- coding: utf-8 -*-
from django.test import TestCase


class WrappingTestCase(TestCase):
    def test_text_view(self):
        real_response = self.client.get('/text/')
        wrapped_response = self.client.get('/__ddte__/text/')

        self.assert_response_wrapped(real_response, wrapped_response)

    def test_templated_response(self):
        real_response = self.client.get('/templated/')
        wrapped_response = self.client.get('/__ddte__/templated/')

        self.assert_response_wrapped(real_response, wrapped_response)

    def test_json_response(self):
        real_response = self.client.get('/json/')
        wrapped_response = self.client.get('/__ddte__/json/')
        self.assert_response_wrapped(real_response, wrapped_response)

    def assert_response_wrapped(self, real_resp, wrapped_resp):
        assert wrapped_resp.status_code == 200
        # make sure that there are html tags that wrap response so
        # django debug toolbar has where to inject its code
        assert all([
            '<html' in str(wrapped_resp.content),
            '</html>' in str(wrapped_resp.content)
        ])
