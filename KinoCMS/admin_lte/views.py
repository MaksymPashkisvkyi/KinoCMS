import datetime

from django.apps import apps
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, TemplateView,
                                  UpdateView, ListView)

from .forms import UserForm, CinemaForm, SeoForm, FilmForm, PhotoInlineFormset, HallForm, BackgroundBannerForm, \
    BannerForm, MainBannerFormset, NewsBannerFormset, PageForm, MainPageForm, ContactFormset, ContactsPageForm, \
    ArticleForm


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
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    gallery_query_set = gallery_model.objects.none()

    cinema = CinemaForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.method == 'POST':
        if cinema.is_valid() and seo.is_valid() and formset.is_valid():
            cinema.save(commit=False)
            gallery = gallery_model.objects.create(title=cinema.cleaned_data['title'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            cinema.instance.gallery = gallery
            seo.save()
            cinema.instance.seo = seo.instance
            cinema.save()
            return redirect('admin_cinema')
    else:
        cinema = CinemaForm()
        seo = SeoForm()
        formset = PhotoInlineFormset()
    context = {
        'form': cinema,
        'seo': seo,
        'formset': formset,
        'title': 'Добавить кинотеатр'
    }
    return render(request, 'admin_lte/cinema/cinema_add.html', context=context)


def edit_cinema_view(request, pk):
    cinema_model = apps.get_model('cinema', 'CinemaModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    hall_model = apps.get_model('cinema', 'HallModel')

    cinema_object = get_object_or_404(cinema_model, pk=pk)
    gallery_object = get_object_or_404(gallery_model, pk=cinema_object.gallery.pk)
    gallery_query_set = gallery_object.imagemodel_set.all()
    halls = hall_model.objects.filter(cinema=cinema_object)

    cinema = CinemaForm(instance=cinema_object)
    seo = SeoForm(instance=cinema_object.seo)
    formset = PhotoInlineFormset(queryset=gallery_query_set)

    if request.method == 'POST':
        cinema = CinemaForm(request.POST or None, request.FILES or None, instance=cinema_object)
        seo = SeoForm(request.POST or None, instance=cinema_object.seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
        if cinema.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = gallery_object
                i.save()
            formset.save()
            seo.save()
            cinema.instance.seo = seo.instance
            cinema.save()
            return redirect('admin_cinema')
    context = {
        'form': cinema,
        'seo': seo,
        'formset': formset,
        'halls': halls,
        'pk': pk,
        'admin_edit_hall': 'admin_edit_hall',
        'admin_delete_hall': 'admin_delete_hall',
        'title': 'Редактировать кинотеатр'
    }
    return render(request, 'admin_lte/cinema/cinema_edit.html', context)


class DeleteCinemaView(DeleteView):
    model = apps.get_model('cinema', 'CinemaModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    success_url = reverse_lazy('admin_cinema')
    template_name = 'admin_lte/cinema/cinema_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить кинотеатр'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        gallery = self.gallery_model.objects.get(pk=self.object.gallery.pk)
        self.object.delete()
        seo.delete()
        gallery.delete()
        return HttpResponseRedirect(self.get_success_url())


# ____________________Cinema____________________ #


# ____________________Hall____________________ #

def add_hall_view(request, pk):
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    cinema_model = apps.get_model('cinema', 'CinemaModel')
    gallery_query_set = gallery_model.objects.none()

    hall = HallForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.method == 'POST':
        if hall.is_valid() and seo.is_valid() and formset.is_valid():
            hall.save(commit=False)
            cinema = cinema_model.objects.get(pk=pk)
            gallery = gallery_model.objects.create(title=hall.cleaned_data['title'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            hall.instance.gallery = gallery
            seo.save()
            hall.instance.seo = seo.instance
            hall.instance.cinema = cinema
            hall.save()
            return redirect('admin_edit_cinema', pk=pk)
    else:
        hall = HallForm()
        seo = SeoForm()
        formset = PhotoInlineFormset()
    context = {
        'form': hall,
        'seo': seo,
        'formset': formset,
        'cinema_id': pk,
        'title': 'Добавить зал'
    }
    return render(request, 'admin_lte/cinema/hall_add.html', context=context)


def edit_hall_view(request, pk):
    hall_model = apps.get_model('cinema', 'HallModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    hall_object = get_object_or_404(hall_model, pk=pk)
    gallery_object = get_object_or_404(gallery_model, pk=hall_object.gallery.pk)
    gallery_query_set = gallery_object.imagemodel_set.all()

    hall = HallForm(instance=hall_object)
    seo = SeoForm(instance=hall_object.seo)
    formset = PhotoInlineFormset(queryset=gallery_query_set)

    if request.method == 'POST':
        hall = HallForm(request.POST or None, request.FILES or None, instance=hall_object)
        seo = SeoForm(request.POST or None, instance=hall_object.seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
        if hall.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = gallery_object
                i.save()
            formset.save()
            seo.save()
            hall.instance.seo = seo.instance
            hall.save()
            return redirect('admin_edit_cinema', pk=hall.instance.cinema.pk)
    context = {
        'form': hall,
        'seo': seo,
        'formset': formset,
        'cinema_id': hall.instance.cinema.pk,
        'title': 'Редактировать зал'
    }
    return render(request, 'admin_lte/cinema/hall_edit.html', context)


class DeleteHallView(DeleteView):
    model = apps.get_model('cinema', 'HallModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    template_name = 'admin_lte/cinema/hall_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['cinema_id'] = self.object.cinema_id
        context['title'] = 'Удалить зал'
        return context

    def form_valid(self, form):
        cinema_id = self.object.cinema_id
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(reverse_lazy('admin_edit_cinema', kwargs={'pk': cinema_id}))


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
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    gallery_query_set = gallery_model.objects.none()

    film = FilmForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)
    if request.method == 'POST':
        if film.is_valid() and seo.is_valid() and formset.is_valid():
            film.save(commit=False)
            gallery = gallery_model.objects.create(title=film.cleaned_data['title'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            film.instance.gallery = gallery
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('admin_film')
    else:
        film = FilmForm()
        seo = SeoForm()
        formset = PhotoInlineFormset()
    context = {
        'form': film,
        'seo': seo,
        'formset': formset,
        'title': 'Добавить фильм'
    }
    return render(request, 'admin_lte/cinema/film_add.html', context=context)


def edit_film_view(request, pk):
    film_model = apps.get_model('cinema', 'FilmModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    film_object = get_object_or_404(film_model, pk=pk)
    gallery_object = get_object_or_404(gallery_model, pk=film_object.gallery.pk)
    gallery_query_set = gallery_object.imagemodel_set.all()

    film = FilmForm(instance=film_object)
    seo = SeoForm(instance=film_object.seo)
    formset = PhotoInlineFormset(queryset=gallery_query_set)

    if request.method == 'POST':
        film = FilmForm(request.POST or None, request.FILES or None, instance=film_object)
        seo = SeoForm(request.POST or None, instance=film_object.seo)
        formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

        if film.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = gallery_object
                i.save()
            formset.save()
            seo.save()
            film.instance.seo = seo.instance
            film.save()
            return redirect('admin_film')
    context = {
        'form': film,
        'seo': seo,
        'formset': formset,
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

# ____________________Banners____________________ #


def banners_view(request):
    bg_banner_model = apps.get_model('cinema', 'BackgroundBannerModel')
    banner_model = apps.get_model('cinema', 'BannerModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    bg_banner_obj, _ = bg_banner_model.objects.get_or_create()
    main_banner_obj, _ = banner_model.objects.get_or_create(name='main')
    news_banner_obj, _ = banner_model.objects.get_or_create(name='news')

    main_gallery_obj, is_main_gallery_created = gallery_model.objects.get_or_create(title='main_banner_formset')
    news_gallery_obj, is_news_gallery_created = gallery_model.objects.get_or_create(title='news_banner_formset')

    if main_banner_obj.gallery:
        main_gallery_queryset = main_gallery_obj.imagemodel_set.all()
    else:
        main_gallery_queryset = gallery_model.objects.none()

    if news_banner_obj.gallery:
        news_gallery_queryset = news_gallery_obj.imagemodel_set.all()
    else:
        news_gallery_queryset = gallery_model.objects.none()

    bg_banner_form = BackgroundBannerForm(request.POST or None, request.FILES or None, instance=bg_banner_obj)
    main_banner_form = BannerForm(request.POST or None, request.FILES or None, instance=main_banner_obj, prefix='main')
    news_banner_form = BannerForm(request.POST or None, request.FILES or None, instance=news_banner_obj, prefix='news')

    main_banner_formset = MainBannerFormset(request.POST or None, request.FILES or None, queryset=main_gallery_queryset,
                                            prefix='main')
    news_banner_formset = NewsBannerFormset(request.POST or None, request.FILES or None, queryset=news_gallery_queryset,
                                            prefix='news')
    if request.method == 'POST':
        if 'bg_banner_form' in request.POST:
            if bg_banner_form.is_valid():
                bg_banner_form.save()
                return redirect('admin_banner')

        if 'main_banner_form' in request.POST:
            if main_banner_form.is_valid() and main_banner_formset.is_valid():
                if is_main_gallery_created:
                    main_gallery_obj.save()
                    for form in main_banner_formset:
                        if form.instance.image:
                            form.save(commit=False)
                            form.instance.gallery = main_gallery_obj
                            form.save()
                    main_banner_form.instance.gallery = main_gallery_obj
                else:
                    main_banner_formset.save(commit=False)
                    for i in main_banner_formset.new_objects:
                        i.gallery = main_gallery_obj
                        i.save()
                    main_banner_formset.save()
                main_banner_form.save()
                return redirect('admin_banner')

        if 'news_banner_form' in request.POST:
            if news_banner_form.is_valid() and news_banner_formset.is_valid():
                if is_news_gallery_created:
                    news_gallery_obj.save()
                    for form in news_banner_formset:
                        if form.instance.image:
                            form.save(commit=False)
                            form.instance.gallery = news_gallery_obj
                            form.save()
                    news_banner_form.instance.gallery = news_gallery_obj
                else:
                    news_banner_formset.save(commit=False)
                    for i in news_banner_formset.new_objects:
                        i.gallery = news_gallery_obj
                        i.save()
                    news_banner_formset.save()
                news_banner_form.save()
                return redirect('admin_banner')

    context = {
        'bg_banner_form': bg_banner_form,
        'main_banner_form': main_banner_form,
        'news_banner_form': news_banner_form,
        'main_banner_formset': main_banner_formset,
        'news_banner_formset': news_banner_formset
    }
    return render(request, 'admin_lte/cinema/banners.html', context)


# ____________________Banners____________________ #


# ____________________Pages____________________ #

class AdminPageView(ListView):
    template_name = 'admin_lte/cinema/page_list.html'
    model = apps.get_model('cinema', 'PageModel')
    main_page_model = apps.get_model('cinema', 'MainPageModel')
    contacts_page_model = apps.get_model('cinema', 'ContactsPageModel')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список страниц'
        context['admin_edit_page'] = 'admin_edit_page'
        context['admin_delete_page'] = 'admin_delete_page'
        context['main_page'], _ = self.main_page_model.objects.get_or_create(title='Главная страница')
        context['contacts'], _ = self.contacts_page_model.objects.get_or_create(title='Контакты')
        context['page_list'] = self.model.objects.order_by('-pk')
        return context


def add_page_view(request):
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    gallery_query_set = gallery_model.objects.none()

    page = PageForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.method == 'POST':
        if page.is_valid() and seo.is_valid() and formset.is_valid():
            page.save(commit=False)
            gallery = gallery_model.objects.create(title=page.cleaned_data['title'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            page.instance.gallery = gallery
            seo.save()
            page.instance.seo = seo.instance
            page.save()
            return redirect('admin_pages')

    context = {
        'form': page,
        'seo': seo,
        'formset': formset,
        'title': 'Добавить страницу'
    }
    return render(request, 'admin_lte/cinema/page_add.html', context=context)


def edit_page_view(request, pk):
    page_model = apps.get_model('cinema', 'PageModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    page_object = get_object_or_404(page_model, pk=pk)
    gallery_object = get_object_or_404(gallery_model, pk=page_object.gallery.pk)
    gallery_query_set = gallery_object.imagemodel_set.all()

    page = PageForm(request.POST or None, request.FILES or None, instance=page_object)
    seo = SeoForm(request.POST or None, request.FILES or None, instance=page_object.seo)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.method == 'POST':
        if page.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = gallery_object
                i.save()
            formset.save()
            seo.save()
            page.instance.seo = seo.instance
            page.save()
            return redirect('admin_pages')

    context = {
        'form': page,
        'seo': seo,
        'formset': formset,
        'title': 'Cоздание страницы'
    }
    return render(request, 'admin_lte/cinema/page_edit.html', context)


class DeletePageView(DeleteView):
    model = apps.get_model('cinema', 'PageModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    success_url = reverse_lazy('admin_pages')
    template_name = 'admin_lte/cinema/page_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['title'] = 'Удалить страницу'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())


def edit_main_page_view(request, pk):
    main_page_model = apps.get_model('cinema', 'MainPageModel')
    main_page_object = get_object_or_404(main_page_model, pk=pk)

    main_page = MainPageForm(request.POST or None, request.FILES or None, instance=main_page_object)
    seo = SeoForm(request.POST or None, request.FILES or None, instance=main_page_object.seo)

    if request.method == 'POST':
        if main_page.is_valid() and seo.is_valid():
            seo.save()
            main_page.instance.seo = seo.instance
            main_page.save()
            return redirect('admin_pages')
    context = {
        'form': main_page,
        'seo': seo,
        'title': 'Главная страница'
    }
    return render(request, 'admin_lte/cinema/main_page_edit.html', context)


def edit_contact_view(request):
    contacts_page_model = apps.get_model('cinema', 'ContactsPageModel')
    contact_model = apps.get_model('cinema', 'ContactModel')

    contact_query_set = contact_model.objects.all()
    contacts_page_object = contacts_page_model.objects.get(title='Контакты')

    seo = SeoForm(request.POST or None, instance=contacts_page_object.seo)
    contacts_page_form = ContactsPageForm(request.POST or None, instance=contacts_page_object)
    formset = ContactFormset(request.POST or None, request.FILES or None, queryset=contact_query_set, prefix='contact')

    if request.method == 'POST':
        if seo.is_valid() and formset.is_valid() and contacts_page_form.is_valid():

            instances = formset.save(commit=False)
            for instance in instances:
                instance.contacts_page = contacts_page_object
                instance.save()
            formset.save()

            seo.save()
            contacts_page_form.instance.seo = seo.instance
            contacts_page_form.save()
            return redirect('admin_pages')
    context = {
        'contacts_page_form': contacts_page_form,
        'seo': seo,
        'formset': formset,
        'title': 'Редактировать контакты'
    }
    return render(request, 'admin_lte/cinema/contact_edit.html', context)


# ____________________Pages____________________ #

# ____________________Articles____________________ #

class AdminArticleView(ListView):
    template_name = 'admin_lte/cinema/article_list.html'
    model = apps.get_model('cinema', 'ArticleModel')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        path = self.request.META.get('PATH_INFO', None)

        context['admin_edit_article'] = 'admin_edit_article'
        context['admin_delete_article'] = 'admin_delete_article'

        if path == '/admin/promo/':
            context['title'] = 'Список акций'
            context['article_list'] = self.model.objects.filter(mode='PROMO').order_by('-pk')
        else:
            context['title'] = 'Список новостей'
            context['article_list'] = self.model.objects.filter(mode='NEWS').order_by('-pk')

        return context


def add_article_view(request):
    gallery_model = apps.get_model('cinema', 'GalleryModel')
    gallery_query_set = gallery_model.objects.none()

    article = ArticleForm(request.POST or None, request.FILES or None)
    seo = SeoForm(request.POST or None)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if request.path == '/admin/promo/add/':
        mode = 'PROMO'
        title = 'Создать акцию'
    else:
        mode = 'NEWS'
        title = 'Создать новость'

    if request.method == 'POST':
        if article.is_valid() and seo.is_valid() and formset.is_valid():
            article.save(commit=False)
            gallery = gallery_model.objects.create(title=article.cleaned_data['title'])
            gallery.save()
            for form in formset:
                if form.instance.image:
                    form.save(commit=False)
                    form.instance.gallery = gallery
                    form.save()
            article.instance.gallery = gallery
            article.instance.mode = mode
            seo.save()
            article.instance.seo = seo.instance
            article.save()
            if mode == 'PROMO':
                return redirect('admin_promo')
            else:
                return redirect('admin_news')
    context = {
        'form': article,
        'seo': seo,
        'formset': formset,
        'title': title
    }
    return render(request, 'admin_lte/cinema/article_add.html', context=context)


def edit_article_view(request, pk):
    page_model = apps.get_model('cinema', 'ArticleModel')
    gallery_model = apps.get_model('cinema', 'GalleryModel')

    article_object = get_object_or_404(page_model, pk=pk)
    gallery_object = get_object_or_404(gallery_model, pk=article_object.gallery.pk)
    gallery_query_set = gallery_object.imagemodel_set.all()

    article = ArticleForm(request.POST or None, request.FILES or None, instance=article_object)
    seo = SeoForm(request.POST or None, request.FILES or None, instance=article_object.seo)
    formset = PhotoInlineFormset(request.POST or None, request.FILES or None, queryset=gallery_query_set)

    if article_object.mode == 'PROMO':
        mode = 'PROMO'
        title = 'Редактировать акцию'
    else:
        mode = 'NEWS'
        title = 'Редактировать новость'

    if request.method == 'POST':
        if article.is_valid() and seo.is_valid() and formset.is_valid():
            formset.save(commit=False)
            for i in formset.new_objects:
                i.gallery = gallery_object
                i.save()
            formset.save()
            seo.save()
            article.instance.seo = seo.instance
            article.save()

            if mode == 'PROMO':
                return redirect('admin_promo')
            else:
                return redirect('admin_news')
    context = {
        'form': article,
        'seo': seo,
        'formset': formset,
        'title': title
    }
    return render(request, 'admin_lte/cinema/article_edit.html', context)


class DeleteArticleView(DeleteView):
    model = apps.get_model('cinema', 'ArticleModel')
    seo_model = apps.get_model('cinema', 'SeoModel')
    template_name = 'admin_lte/cinema/article_delete.html'
    success_url = reverse_lazy('admin_promo')

    def get_success_url(self):
        mode = self.object.mode
        if mode == 'POST':
            return reverse_lazy('admin_promo')
        else:
            return reverse_lazy('admin_news')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        mode = self.object.mode
        context['form'] = self.model.objects.get(pk=self.kwargs['pk'])
        if mode == 'POST':
            context['title'] = 'Удалить акцию'
        else:
            context['title'] = 'Удалить новость'
        return context

    def form_valid(self, form):
        seo = self.seo_model.objects.get(pk=self.object.seo.pk)
        self.object.delete()
        seo.delete()
        return HttpResponseRedirect(self.get_success_url())

# ____________________Articles____________________ #
