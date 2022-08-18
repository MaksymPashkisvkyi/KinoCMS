from django.shortcuts import render
from django.views.generic import TemplateView
from django.apps import apps


def admin_statistic(request):
    template_name = 'admin_lte/admin/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


class AdminCinemaView(TemplateView):
    template_name = 'admin_lte/cinema/cinemas.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'CinemaModel')

        context = super().get_context_data()
        context['title'] = 'Кинотеатры'
        context['cinemas'] = model.objects.all()

        return context


class AdminHallView(TemplateView):
    template_name = 'admin_lte/cinema/halls.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'HallModel')

        context = super().get_context_data()
        context['title'] = 'Залы'
        context['halls'] = model.objects.all()

        return context


class AdminFilmView(TemplateView):
    template_name = 'admin_lte/cinema/films.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'FilmModel')

        context = super().get_context_data()
        context['title'] = 'Фильмы'
        context['films'] = model.objects.all()

        return context


class AdminSessionView(TemplateView):
    template_name = 'admin_lte/cinema/sessions.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'SessionModel')

        context = super().get_context_data()
        context['title'] = 'Сессии'
        context['sessions'] = model.objects.all()

        return context


class AdminTicketView(TemplateView):
    template_name = 'admin_lte/cinema/tickets.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('user', 'TicketModel')

        context = super().get_context_data()
        context['title'] = 'Билеты'
        context['tickets'] = model.objects.all()

        return context


class AdminSEOView(TemplateView):
    template_name = 'admin_lte/admin/seo.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'SEOModel')

        context = super().get_context_data()
        context['title'] = 'SEO'
        context['seo_s'] = model.objects.all()

        return context


class AdminGalleryView(TemplateView):
    template_name = 'admin_lte/admin/gallery.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'GalleryModel')

        context = super().get_context_data()
        context['title'] = 'Галерея'
        context['galleries'] = model.objects.all()

        return context


class AdminUserView(TemplateView):
    template_name = 'admin_lte/user/users.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('user', 'UserModel')

        context = super().get_context_data()
        context['title'] = 'Пользователи'
        context['users'] = model.objects.all()

        return context


class AdminBannerView(TemplateView):
    template_name = 'admin_lte/banner/banners.html'

    def get_context_data(self, **kwargs):
        model = {
            'BackgroundBannerModel': apps.get_model('banners', 'BackgroundBannerModel'),
            'MainPageBannerModel': apps.get_model('banners', 'MainPageBannerModel'),
            'NewsPromoBannerModel': apps.get_model('banners', 'NewsPromoBannerModel'),
            'BannerConfigModel': apps.get_model('banners', 'BannerConfigModel')
        }

        context = super().get_context_data()
        context['title'] = 'banners'
        context['background_banners'] = model['BackgroundBannerModel'].objects.all()
        context['main_page_banners'] = model['MainPageBannerModel'].objects.all()
        context['new_promo_banners'] = model['NewsPromoBannerModel'].objects.all()
        context['banner_configs'] = model['BannerConfigModel'].objects.all()

        return context


class AdminBannerConfigView(TemplateView):
    template_name = 'admin_lte/banner/banner_config.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'BannerConfigModel')

        context = super().get_context_data()
        context['title'] = 'banner_configs'
        context['banner_configs'] = model.objects.all()

        return context


class AdminBackgroundBannerView(TemplateView):
    template_name = 'admin_lte/banner/background_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'BackgroundBannerModel')

        context = super().get_context_data()
        context['title'] = 'BackgroundBannerModel'
        context['background_banners'] = model.objects.all()

        return context


class AdminMainPageBannerView(TemplateView):
    template_name = 'admin_lte/banner/main_page_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'MainPageBannerModel')

        context = super().get_context_data()
        context['title'] = 'MainPageBannerModel'
        context['main_page_banners'] = model.objects.all()

        return context


class AdminNewsPromoBannerView(TemplateView):
    template_name = 'admin_lte/banner/new_promo_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'NewsPromoBannerModel')

        context = super().get_context_data()
        context['title'] = 'NewsPromoBannerModel'
        context['new_promo_banners'] = model.objects.all()

        return context
