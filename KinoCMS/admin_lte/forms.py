from django import forms
from django.apps import apps

from .utils import CITIES, LANGS, GENDERS


class CinemaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo'].empty_label = 'Логотип не выбран'
        self.fields['banner_image'].empty_label = 'Фото верхнего баннера не выбрано'
        self.fields['seo_block'].empty_label = 'SEO блок не выбран'

    class Meta:
        model = apps.get_model('cinema', 'CinemaModel')
        fields = ['name', 'description', 'condition', 'logo', 'banner_image', 'gallery', 'seo_block']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название кинотеатра'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Описание кинотеатра'}),
            'condition': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Условия кинотеатра'})
        }


class HallForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cinema'].empty_label = 'Кинотеатр не выбран'
        self.fields['banner_image'].empty_label = 'Фото верхнего баннера не выбрано'
        self.fields['seo_block'].empty_label = 'SEO блок не выбран'

    class Meta:
        model = apps.get_model('cinema', 'HallModel')
        fields = ['name', 'description', 'hall_scheme', 'cinema', 'banner_image', 'gallery', 'seo_block']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер зала'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Описание зала'})
        }


class SEOForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'SEOModel')
        fields = ['URL', 'title', 'keywords', 'description']
        widgets = {
            'URL': forms.URLInput(attrs={'placeholder': 'Ссылка на страницу'}),
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Оглавление'}),
            'keywords': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Ключевые слова'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Описание блока'})
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'GalleryModel')
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название изображения'})
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = ['name', 'surname', 'nickname', 'email', 'address', 'password', 'repeat_password', 'card_number',
                  'language', 'gender', 'phone', 'date', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'surname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия'}),
            'nickname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Псевдоним'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'address': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Адресс'}),
            'password': forms.PasswordInput(attrs={'placeholder': ''}),
            'repeat_password': forms.PasswordInput(attrs={'placeholder': ''}),
            'card_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер карты'}),
            'language': forms.RadioSelect(choices=LANGS),
            'gender': forms.RadioSelect(choices=GENDERS),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+380-00-00-00-000'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Дата рождения'}),
            'city': forms.Select(choices=CITIES),
        }


class FilmForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['main_image'].empty_label = 'Главное изображение не выбрано'
        self.fields['seo_block'].empty_label = 'SEO блок не выбран'

    class Meta:
        model = apps.get_model('cinema', 'FilmModel')
        fields = ['name', 'description', 'main_image', 'gallery', 'URL', 'three_D', 'two_D', 'IMAX', 'seo_block']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название фильма'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Описание фильма'}),
            'URL': forms.URLInput(attrs={'placeholder': 'Ссылка на фильм'})
        }
