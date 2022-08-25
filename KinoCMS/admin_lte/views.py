from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.apps import apps

from .forms import CinemaForm, HallForm, UserForm, FilmForm


def admin_statistic(request):
    template_name = 'admin_lte/admin/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


class AddCinemaView(CreateView):
    form_class = CinemaForm
    template_name = 'admin_lte/cinema/add_cinema.html'
    success_url = reverse_lazy('admin_cinema')

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'HallModel')
        context = super().get_context_data()
        context['title'] = 'Добавить кинотеатр'
        context['halls'] = model.objects.all()
        return context


class EditCinemaView(UpdateView):
    model = apps.get_model('cinema', 'CinemaModel')
    form_class = CinemaForm
    template_name = 'admin_lte/cinema/edit_cinema.html'
    success_url = reverse_lazy('admin_cinema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Редактировать кинотеатр'
        return context

    def get_queryset(self):
        model = apps.get_model('cinema', 'CinemaModel')
        return model.objects.filter(pk=self.kwargs['pk'])


class DeleteCinemaView(DeleteView):
    model = apps.get_model('cinema', 'CinemaModel')
    success_url = reverse_lazy('admin_cinema')
    # model = apps.get_model('cinema', 'CinemaModel')
    # form_class = CinemaForm
    template_name = 'admin_lte/cinema/delete_cinema.html'
    # success_url = reverse_lazy('admin_cinema')
    #
    # def get_context_data(self, **kwargs):
    #     model = apps.get_model('cinema', 'CinemaModel')
    #     context = super().get_context_data()
    #     context['cinema'] = model.objects.get(pk=self.kwargs['pk'])
    #     context['title'] = 'Удалить кинотеатр'
    #     return context
    #
    # def get_queryset(self):
    #     model = apps.get_model('cinema', 'CinemaModel')
    #     return model.objects.filter(pk=self.kwargs['pk'])
    # pass


class AddHallView(CreateView):
    form_class = HallForm
    template_name = 'admin_lte/cinema/add_hall.html'
    success_url = reverse_lazy('admin_add_cinema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить зал'
        return context


class AddUserView(CreateView):
    form_class = UserForm
    template_name = 'admin_lte/user/add_user.html'
    success_url = reverse_lazy('admin_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Профиль пользователя'
        return context


class AddFilmView(CreateView):
    form_class = FilmForm
    template_name = 'admin_lte/cinema/add_film.html'
    success_url = reverse_lazy('admin_film')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить фильм'
        return context


class AdminCinemaView(TemplateView):
    template_name = 'admin_lte/cinema/cinemas.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'CinemaModel')

        context = super().get_context_data()
        context['title'] = 'Кинотеатры'
        context['cinemas'] = model.objects.all()

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
        context['title'] = 'Баннера/Слайдеры'
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
        context['banner_configs'] = model.objects.all()

        return context


class AdminBackgroundBannerView(TemplateView):
    template_name = 'admin_lte/banner/background_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'BackgroundBannerModel')

        context = super().get_context_data()
        context['background_banners'] = model.objects.all()

        return context


class AdminMainPageBannerView(TemplateView):
    template_name = 'admin_lte/banner/main_page_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'MainPageBannerModel')

        context = super().get_context_data()
        context['main_page_banners'] = model.objects.all()

        return context


class AdminNewsPromoBannerView(TemplateView):
    template_name = 'admin_lte/banner/new_promo_banner.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('banners', 'NewsPromoBannerModel')

        context = super().get_context_data()
        context['new_promo_banners'] = model.objects.all()

        return context
