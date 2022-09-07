import datetime

from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, TemplateView,
                                  UpdateView, ListView)

from .forms import HallMultiForm, UserForm, CinemaForm, SeoForm, FilmForm


def admin_statistic(request):
    template_name = 'admin_lte/admin/statistic.html'
    context = {
        'title': 'Статистика'
    }
    return render(request, template_name, context)


# ____________________Cinema____________________ #

class AdminCinemaView(ListView):
    model = apps.get_model('cinema', 'CinemaModel')
    template_name = 'admin_lte/cinema/cinema_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список кинотеатров'
        context['cinema_list'] = self.model.objects.order_by('-pk')
        return context


def add_cinema_view(request):
    cinema = CinemaForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)

    if request.method == 'POST':
        if cinema.is_valid() and seo.is_valid():
            cinema.save(commit=False)
            seo.save()
            cinema.instance.seo = seo.instance
            cinema.save()
            return redirect('admin_cinema')

    context = {
        'form': cinema,
        'seo': seo,
        'title': 'Добавить кинотеатр'
    }
    return render(request, 'admin_lte/cinema/cinema_add.html', context=context)


def edit_cinema_view(request, pk):
    model = apps.get_model('cinema', 'CinemaModel')
    obj = get_object_or_404(model, pk=pk)
    cinema = CinemaForm(instance=obj)
    seo = SeoForm(instance=obj.seo)
    if request.method == 'POST':
        cinema = CinemaForm(request.POST, request.FILES, instance=obj)
        seo = SeoForm(request.POST, request.FILES, instance=obj.seo)
        if cinema.is_valid() and seo.is_valid():
            cinema.save(commit=False)
            seo.save()
            cinema.instance.seo = seo.instance
            cinema.save()
            return redirect('admin_cinema')
    context = {
        'form': cinema,
        'seo': seo,
        'title': 'Редактировать кинотеатр'
    }
    return render(request, 'admin_lte/cinema/cinema_edit.html', context)


class DeleteCinemaView(DeleteView):
    model = apps.get_model('cinema', 'CinemaModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    success_url = reverse_lazy('admin_cinema')
    template_name = 'admin_lte/cinema/cinema_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить кинотеатр'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
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
        hall.seo = seo
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
            'seo': self.object.seo,
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Редактировать зал'
        return context


class DeleteHallView(DeleteView):
    model = apps.get_model('cinema', 'HallModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    success_url = reverse_lazy('admin_add_cinema')
    template_name = 'admin_lte/cinema/delete_hall.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['hall'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить зал'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())


# ____________________Hall____________________ #


# ____________________Film____________________ #

class AdminFilmView(ListView):
    template_name = 'admin_lte/cinema/film_list.html'
    model = apps.get_model('cinema', 'FilmModel')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список фильмов'
        context['film_actual'] = self.model.objects.filter(release_date__lte=datetime.date.today())
        context['film_soon'] = self.model.objects.filter(release_date__gt=datetime.date.today())
        return context


def add_film_view(request):
    film = FilmForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)

    if request.method == 'POST':
        if film.is_valid() and seo.is_valid():
            print(film.cleaned_data)
            film.save(commit=False)
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('admin_film')

    context = {
        'form': film,
        'seo': seo,
        'title': 'Добавить фильм'
    }
    return render(request, 'admin_lte/cinema/film_add.html', context=context)


def edit_film_view(request, pk):
    model = apps.get_model('cinema', 'FilmModel')
    obj = get_object_or_404(model, pk=pk)
    film = FilmForm(instance=obj)
    seo = SeoForm(instance=obj.seo)
    if request.method == 'POST':
        film = FilmForm(request.POST, request.FILES, instance=obj)
        seo = SeoForm(request.POST, request.FILES, instance=obj.seo)
        if film.is_valid() and seo.is_valid():
            film.save(commit=False)
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('admin_film')
    context = {
        'form': film,
        'seo': seo,
        'title': 'Редактировать фильм'
    }
    return render(request, 'admin_lte/cinema/film_edit.html', context)


class DeleteFilmView(DeleteView):
    model = apps.get_model('cinema', 'FilmModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    success_url = reverse_lazy('admin_film')
    template_name = 'admin_lte/cinema/film_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить фильм'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())


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
