from betterforms.multiform import MultiModelForm
from django import forms
from django.apps import apps

from .utils import CITIES, GENDERS, LANGS


class SeoForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'SeoModel')
        fields = ['url', 'title', 'keywords', 'description']
        widgets = {
            'url': forms.URLInput(attrs={
                'placeholder': 'Ссылка на страницу'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Оглавление'
            }),
            'keywords': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Ключевые слова'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Описание блока'
            })
        }
        labels = {
            'title': 'Заголовок',
            'url': 'URL-адрес',
            'keywords': 'Ключевые слова',
            'description': 'Описание',
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'GalleryModel')
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название изображения'
            })
        }


class CinemaForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'CinemaModel')
        fields = ['title', 'description', 'condition', 'logo', 'banner', 'gallery']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название кинотеатра'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Описание кинотеатра'
            }),
            'condition': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Условия кинотеатра'
            })
        }
        labels = {
            'title': 'Название кинотеатра',
            'description': 'Описание',
            'condition': 'Условия',
            'logo': 'Логотип',
            'banner': 'Фото верхнего баннера',
            'gallery': 'Галерея картинок'
        }


class HallForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'HallModel')
        fields = ['title', 'description', 'hall_scheme', 'banner', 'gallery']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Номер зала'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Описание зала'
            })
        }
        labels = {
            'title': 'Номер зала',
            'description': 'Описание зала',
            'hall_scheme': 'Схема зала',
            'banner': 'Верхний баннер',
            'gallery': 'Галерея картинок'
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = ['name', 'surname', 'nickname', 'email', 'address', 'password', 'repeat_password', 'card_number',
                  'language', 'gender', 'phone', 'date', 'city']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Имя'
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Фамилия'
            }),
            'nickname': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Псевдоним'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Адресс'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': ''
            }),
            'repeat_password': forms.PasswordInput(attrs={
                'placeholder': ''
            }),
            'card_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Номер карты'
            }),
            'language': forms.RadioSelect(choices=LANGS),
            'gender': forms.RadioSelect(choices=GENDERS),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+380-00-00-00-000'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Дата рождения'
            }),
            'city': forms.Select(choices=CITIES),
        }
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'nickname': 'Псевдоним',
            'address': 'E-mail',
            'email': 'Адресс',
            'password': 'Пароль',
            'repeat_password': 'Повторить пароль',
            'card_number': 'Номер карты',
            'gender': 'Пол',
            'phone': 'Телефон',
            'date': 'Дата рождения',
            'city': 'Город',
        }


class FilmForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'FilmModel')
        fields = ['title', 'description', 'poster', 'gallery', 'url', 'is_3d', 'is_2d', 'is_imax']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название фильма'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Описание фильма'
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'Ссылка на видео в YouTube'
            })
        }
        labels = {
            'title': 'Название фильма',
            'description': 'Описание',
            'poster': 'Главная картинка',
            'gallery': 'Галерея картинок',
            'url': 'Ссылка на трейлер',
            'is_3d': '3D',
            'is_2d': '2D',
            'is_imax': 'IMAX'
        }


class CinemaMultiForm(MultiModelForm):
    form_classes = {
        'cinema': CinemaForm,
        'seo': SeoForm
    }

    def save(self, commit=True):
        objects = super(CinemaMultiForm, self).save(commit=False)
        if commit:
            seo = objects['seo']
            seo.save()
            cinema = objects['cinema']
            cinema.seo_block = seo
            cinema.save()
        return objects


class HallMultiForm(MultiModelForm):
    form_classes = {
        'hall': HallForm,
        'seo': SeoForm
    }

    def save(self, commit=True):
        objects = super(HallMultiForm, self).save(commit=False)
        if commit:
            seo = objects['seo']
            seo.save()
            hall = objects['hall']
            hall.seo_block = seo
            hall.save()
        return objects
