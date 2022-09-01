from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
    template_name = "pages/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class PosterView(TemplateView):
    template_name = "pages/poster.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Афиша'
        return context


class SoonView(TemplateView):
    template_name = "pages/soon.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Скоро'
        return context


class ScheduleView(TemplateView):
    template_name = "pages/schedule.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расписание'
        return context


class PromoView(TemplateView):
    template_name = "pages/promo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Акции'
        return context


class CinemasView(TemplateView):
    template_name = "pages/cinemas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Кинотеатры'
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О кинотеатре'
        return context


class AdvertisementView(TemplateView):
    template_name = "pages/advertisement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Реклама'
        return context


class CafeView(TemplateView):
    template_name = "pages/cafe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Кафе'
        return context


class ContactsView(TemplateView):
    template_name = "pages/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class MobileAppsView(TemplateView):
    template_name = "pages/mobile_apps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мобильное приложение'
        return context


class NewsView(TemplateView):
    template_name = "pages/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context
