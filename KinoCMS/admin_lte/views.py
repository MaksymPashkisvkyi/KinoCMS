from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, TemplateView,
                                  UpdateView)

from .forms import CinemaMultiForm, FilmForm, HallMultiForm, UserForm


def admin_statistic(request):
    template_name = 'admin_lte/admin/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


# ____________________Cinema____________________ #

class AdminCinemaView(TemplateView):
    template_name = 'admin_lte/cinema/cinemas.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'CinemaModel')
        context = super().get_context_data()
        context['title'] = 'Кинотеатры'
        context['admin_edit_cinema'] = 'admin_edit_cinema'
        context['admin_delete_cinema'] = 'admin_delete_cinema'
        context['cinemas'] = model.objects.all()
        return context


class AddCinemaView(CreateView):
    form_class = CinemaMultiForm
    model = apps.get_model('cinema', 'CinemaModel')
    success_url = reverse_lazy('admin_cinema')
    template_name = 'admin_lte/cinema/add_edit_cinema.html'

    def get_context_data(self, **kwargs):
        hall_model = apps.get_model('cinema', 'HallModel')
        context = super().get_context_data()
        context['title'] = 'Добавить кинотеатр'
        context['admin_edit_hall'] = 'admin_edit_hall'
        context['admin_delete_hall'] = 'admin_delete_hall'
        context['halls'] = hall_model.objects.all()
        return context

    def form_valid(self, form):
        seo = form['seo'].save()
        cinema = form['cinema'].save(commit=False)
        cinema.seo_block = seo
        cinema.save()
        return redirect('admin_cinema')


class EditCinemaView(UpdateView):
    form_class = CinemaMultiForm
    model = apps.get_model('cinema', 'CinemaModel')
    success_url = reverse_lazy('admin_cinema')
    template_name = 'admin_lte/cinema/add_edit_cinema.html'

    def get_form_kwargs(self):
        kwargs = super(EditCinemaView, self).get_form_kwargs()
        kwargs.update(instance={
            'cinema': self.object,
            'seo': self.object.seo_block,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        hall_model = apps.get_model('cinema', 'HallModel')
        context = super().get_context_data()
        context['title'] = 'Редактировать кинотеатр'
        context['admin_edit_hall'] = 'admin_edit_hall'
        context['admin_delete_hall'] = 'admin_delete_hall'
        context['halls'] = hall_model.objects.all()
        return context


class DeleteCinemaView(DeleteView):
    model = apps.get_model('cinema', 'CinemaModel')
    seo_model = apps.get_model('cinema', 'SEOModel')
    success_url = reverse_lazy('admin_cinema')
    template_name = 'admin_lte/cinema/delete_cinema.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cinema'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить кинотеатр'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo_block.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())


# ____________________Cinema____________________ #


# ____________________Hall____________________ #

class AddHallView(CreateView):
    form_class = HallMultiForm
    template_name = 'admin_lte/cinema/add_edit_hall.html'
    success_url = reverse_lazy('admin_add_cinema')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить зал'
        return context

    def form_valid(self, form):
        seo = form['seo'].save()
        hall = form['hall'].save(commit=False)
        hall.seo_block = seo
        hall.save()
        return redirect('admin_add_cinema')


class EditHallView(UpdateView):
    form_class = HallMultiForm
    model = apps.get_model('cinema', 'HallModel')
    template_name = 'admin_lte/cinema/add_edit_hall.html'
    success_url = reverse_lazy('admin_add_cinema')

    def get_form_kwargs(self):
        kwargs = super(EditHallView, self).get_form_kwargs()
        kwargs.update(instance={
            'hall': self.object,
            'seo': self.object.seo_block,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Редактировать зал'
        return context


class DeleteHallView(DeleteView):
    model = apps.get_model('cinema', 'HallModel')
    seo_model = apps.get_model('cinema', 'SEOModel')
    success_url = reverse_lazy('admin_add_cinema')
    template_name = 'admin_lte/cinema/delete_hall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['hall'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить зал'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo_block.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())


# ____________________Hall____________________ #


# ____________________Film____________________ #

class AdminFilmView(TemplateView):
    template_name = 'admin_lte/cinema/films.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('cinema', 'FilmModel')

        context = super().get_context_data()
        context['title'] = 'Фильмы'
        context['films'] = model.objects.all()

        return context


class AddFilmView(CreateView):
    form_class = FilmForm
    template_name = 'admin_lte/cinema/add_film.html'
    success_url = reverse_lazy('admin_film')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить фильм'
        return context


class EditFilmView(UpdateView):
    pass


class DeleteFilmView(DeleteView):
    pass


# ____________________Film____________________ #


# ____________________User____________________ #

class AdminUserView(TemplateView):
    template_name = 'admin_lte/user/users.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('user', 'UserModel')

        context = super().get_context_data()
        context['title'] = 'Пользователи'
        context['admin_edit_user'] = 'admin_edit_user'
        context['admin_delete_user'] = 'admin_delete_user'
        context['users'] = model.objects.all()

        return context


class AddUserView(CreateView):
    form_class = UserForm
    template_name = 'admin_lte/user/add_edit_user.html'
    success_url = reverse_lazy('admin_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добавить профиль пользователя'
        return context


class EditUserView(UpdateView):
    model = apps.get_model('user', 'UserModel')
    form_class = UserForm
    template_name = 'admin_lte/user/add_edit_user.html'
    success_url = reverse_lazy('admin_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Редактировать профиль пользователя'
        return context

    def get_queryset(self):
        model = apps.get_model('user', 'UserModel')
        return model.objects.filter(pk=self.kwargs['pk'])


class DeleteUserView(DeleteView):
    model = apps.get_model('user', 'UserModel')
    success_url = reverse_lazy('admin_user')
    template_name = 'admin_lte/user/delete_user.html'

    def get_context_data(self, **kwargs):
        model = apps.get_model('user', 'UserModel')
        context = super().get_context_data()
        context['user'] = model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить профиль пользователя'
        return context


# ____________________User____________________ #


class AdminBannerView(TemplateView):
    template_name = 'admin_lte/banner/banners.html'

    def get_context_data(self, **kwargs):
        model = {
            'BackgroundBannerModel': apps.get_model('banners', 'BackgroundBannerModel'),
            'MainPageBannerModel': apps.get_model('banners', 'MainPageBannerModel'),
            'NewsPromoBannerModel': apps.get_model('banners', 'NewsPromoBannerModel')
        }

        context = super().get_context_data()
        context['title'] = 'Баннера/Слайдеры'
        context['background_banners'] = model['BackgroundBannerModel'].objects.all()
        context['main_page_banners'] = model['MainPageBannerModel'].objects.all()
        context['new_promo_banners'] = model['NewsPromoBannerModel'].objects.all()

        return context
