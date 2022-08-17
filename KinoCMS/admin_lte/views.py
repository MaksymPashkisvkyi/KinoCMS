from django.shortcuts import render
from django.views.generic import TemplateView

from .models import CinemaModel, HallModel, FilmModel, SessionModel, TicketModel, UserModel, GalleryModel, SEOModel, \
    BackgroundBannerModel, MainPageBannerModel, NewsPromoBannerModel, BannerConfigModel, MainPageModel, NewsPromoModel, \
    ContactModel, PageModel


# from KinoCMS.cinema.models import SEOModel

def admin_statistic(request):
    template_name = 'admin_lte/admin/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


class AdminCinemaView(TemplateView):
    template_name = 'admin_lte/cinema/cinemas.html'
    model = 'CinemaModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Кинотеатры'
        context['cinemas'] = CinemaModel.objects.all()

        return context


class AdminHallView(TemplateView):
    template_name = 'admin_lte/cinema/halls.html'
    model = 'HallModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Залы'
        context['halls'] = HallModel.objects.all()

        return context


class AdminFilmView(TemplateView):
    template_name = 'admin_lte/cinema/films.html'
    model = 'FilmModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Фильмы'
        context['films'] = FilmModel.objects.all()

        return context


class AdminSessionView(TemplateView):
    template_name = 'admin_lte/cinema/sessions.html'
    model = 'SessionModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Сессии'
        context['sessions'] = SessionModel.objects.all()

        return context


class AdminTicketView(TemplateView):
    template_name = 'admin_lte/cinema/tickets.html'
    model = 'TicketModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Билеты'
        context['tickets'] = TicketModel.objects.all()

        return context


class AdminSEOView(TemplateView):
    template_name = 'admin_lte/admin/seo.html'
    model = 'SEOModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'SEO'
        context['seo_s'] = SEOModel.objects.all()

        return context


class AdminGalleryView(TemplateView):
    template_name = 'admin_lte/admin/gallery.html'
    model = 'GalleryModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Галерея'
        context['galleries'] = GalleryModel.objects.all()

        return context


class AdminUserView(TemplateView):
    template_name = 'admin_lte/user/users.html'
    model = 'UserModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Пользователи'
        context['users'] = UserModel.objects.all()

        return context


class AdminBannerView(TemplateView):
    template_name = 'admin_lte/banner/banners.html'
    # model = 'BannerConfigModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'banners'
        context['background_banners'] = BackgroundBannerModel.objects.all()
        context['main_page_banners'] = MainPageBannerModel.objects.all()
        context['new_promo_banners'] = NewsPromoBannerModel.objects.all()

        return context


class AdminBannerConfigView(TemplateView):
    template_name = 'admin_lte/banner/banner_config.html'
    model = 'BannerConfigModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'banner_configs'
        context['banner_configs'] = BannerConfigModel.objects.all()

        return context


class AdminBackgroundBannerView(TemplateView):
    template_name = 'admin_lte/banner/background_banner.html'
    model = 'BackgroundBannerModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'BackgroundBannerModel'
        context['background_banners'] = BackgroundBannerModel.objects.all()

        return context


class AdminMainPageBannerView(TemplateView):
    template_name = 'admin_lte/banner/main_page_banner.html'
    model = 'MainPageBannerModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'MainPageBannerModel'
        context['main_page_banners'] = MainPageBannerModel.objects.all()

        return context


class AdminNewsPromoBannerView(TemplateView):
    template_name = 'admin_lte/banner/new_promo_banner.html'
    model = 'NewsPromoBannerModel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'NewsPromoBannerModel'
        context['new_promo_banners'] = NewsPromoBannerModel.objects.all()

        return context
#
#
# class AdminUserView(TemplateView):
#     template_name = 'admin_lte/user/users.html'
#     model = 'UserModel'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Пользователи'
#         context['users'] = UserModel.objects.all()
#
#         return context
#
#
# class AdminUserView(TemplateView):
#     template_name = 'admin_lte/user/users.html'
#     model = 'UserModel'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Пользователи'
#         context['users'] = UserModel.objects.all()
#
#         return context
#
#
# class AdminUserView(TemplateView):
#     template_name = 'admin_lte/user/users.html'
#     model = 'UserModel'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Пользователи'
#         context['users'] = UserModel.objects.all()
#
#         return context
#
#
# class AdminUserView(TemplateView):
#     template_name = 'admin_lte/user/users.html'
#     model = 'UserModel'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Пользователи'
#         context['users'] = UserModel.objects.all()
#
#         return context
#
#
# class AdminUserView(TemplateView):
#     template_name = 'admin_lte/user/users.html'
#     model = 'UserModel'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title'] = 'Пользователи'
#         context['users'] = UserModel.objects.all()
#
#         return context
