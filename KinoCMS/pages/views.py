from django.contrib import messages
from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
    template_name = "pages/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
