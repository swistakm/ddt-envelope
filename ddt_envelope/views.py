from django.views.generic import TemplateView
from django.core import urlresolvers

class EnvelopeView(TemplateView):
    template_name = 'ddte/envelope.html'

    def get(self, request, *args, **kwargs):
        url = "/"+kwargs.get("next")
        print url
        target_view = urlresolvers.resolve(url)

        view_response = target_view.func(request, **target_view.kwargs)
        if hasattr(view_response, "render"):
            content = view_response.render()
        else:
            content = view_response

        return self.render_to_response(locals())