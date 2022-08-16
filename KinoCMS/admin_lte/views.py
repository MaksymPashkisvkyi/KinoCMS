from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CinemaModel


def admin_statistic(request):
    template_name = 'admin_lte/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


# def admin_cinema(request):
#     template_name = 'admin_lte/cinema.html'
#     context = {
#         'title': 'Кинотеатры'
#     }
#     return render(request, template_name, context)


class AdminCinemaView(TemplateView):
    template_name = 'admin_lte/cinema.html'
    model = 'CinemaModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Кинотеатры'
        context['cinemas'] = CinemaModel.objects.all()

        return context
