import json

from django.views.generic import TemplateView
from django.core import urlresolvers


class EnvelopeView(TemplateView):
    template_name = 'ddte/envelope.html'

    def get_target_view_response(self, request, path):
        target_view = urlresolvers.resolve(path)

        view_response = target_view.func(
            request,
            **target_view.kwargs
        )
        if hasattr(view_response, "render"):
            content = view_response.render()
        else:
            content = view_response

        return content

    def get(self, request, *args, **kwargs):
        path = "/" + kwargs.get("next")
        target_response = self.get_target_view_response(request, path)

        if self.is_json(target_response):
            content = self.reformat_json(target_response.content)
        else:
            content = target_response.content

        return self.render_to_response({
            'path': path,
            'content': content,
            'response': target_response,
            'headers': dict([
                (header, value) for header, value in target_response.items()
            ]),
        })

    def is_json(self, response):
        return response.get('Content-Type') == 'application/json'

    def reformat_json(self, content):
        # note: in python3 response content might be bytes so we must decode it
        if isinstance(content, bytes):
            raw_content = content.decode('utf-8')
        else:
            raw_content = content

        return json.dumps(json.loads(raw_content), indent=4)
