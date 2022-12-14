from django import forms
from django.apps import apps
from django.forms import modelformset_factory, HiddenInput

from .utils import CITIES, GENDERS, LANGS


class SeoForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'SeoModel')
        fields = ['seo_url', 'seo_title', 'seo_keywords', 'seo_description']
        widgets = {
            'seo_url': forms.URLInput(attrs={
                'placeholder': 'Ссылка на страницу'
            }),
            'seo_title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Оглавление'
            }),
            'seo_keywords': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ключевые слова'
            }),
            'seo_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Описание блока'
            })
        }
        labels = {
            'seo_title': 'Заголовок',
            'seo_url': 'URL-адрес',
            'seo_keywords': 'Ключевые слова',
            'seo_description': 'Описание',
        }


class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput, label='')

    class Meta:
        model = apps.get_model('cinema', 'ImageModel')
        fields = ['image', 'text', 'url']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control'
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


PhotoInlineFormset = modelformset_factory(model=apps.get_model('cinema', 'ImageModel'), form=ImageForm,
                                          fields=('image',), extra=0, can_delete=True)
PhotoInlineFormset.deletion_widget = HiddenInput


class CinemaForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'CinemaModel')
        fields = ['title', 'description', 'condition', 'logo', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название кинотеатра'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Описание кинотеатра'
            }),
            'condition': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Условия кинотеатра'
            }),
            'logo': forms.FileInput(),
            'banner': forms.FileInput()
        }
        labels = {
            'title': 'Название кинотеатра',
            'description': 'Описание',
            'condition': 'Условия',
            'logo': 'Логотип',
            'banner': 'Фото верхнего баннера'
        }


class HallForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'HallModel')
        fields = ['title', 'description', 'hall_scheme', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Номер зала'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Описание зала'
            }),
            'hall_scheme': forms.FileInput(),
            'banner': forms.FileInput(),
        }
        labels = {
            'title': 'Номер зала',
            'description': 'Описание зала',
            'hall_scheme': 'Схема зала',
            'banner': 'Верхний баннер',
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
        fields = ['title', 'description', 'poster', 'url', 'release_date', 'is_active', 'is_3d', 'is_2d',
                  'is_imax']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название фильма'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Описание фильма'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на видео в YouTube'
            }),
            'release_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
            'poster': forms.FileInput()
        }
        labels = {
            'title': 'Название фильма',
            'description': 'Описание',
            'poster': 'Главная картинка',
            'url': 'Ссылка на трейлер',
            'release_date': 'Начало показов',
            'is_active': 'Активно',
            'is_3d': '3D',
            'is_2d': '2D',
            'is_imax': 'IMAX'
        }


class BannerForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'BannerModel')
        fields = ['is_active', 'rotation_speed']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            }),
            'rotation_speed': forms.NumberInput(attrs={
                'class': 'form-control',
                'col': '3'
            })
        }
        labels = {
            'rotation_speed': 'Скорость вращения',
        }


class BackgroundBannerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BackgroundBannerForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['color'].required = False

    class Meta:
        model = apps.get_model('cinema', 'BackgroundBannerModel')
        fields = ['image', 'mode', 'color']
        widgets = {
            'image': forms.FileInput(attrs={
                'data-jscolor': '{}',
            }),
            'mode': forms.RadioSelect(attrs={
                'onclick': 'change_background()',
            })
        }


MainBannerFormset = modelformset_factory(model=apps.get_model('cinema', 'ImageModel'), form=ImageForm,
                                         fields=('image', 'url', 'text',), extra=0, can_delete=True)
NewsBannerFormset = modelformset_factory(model=apps.get_model('cinema', 'ImageModel'), form=ImageForm,
                                         fields=('image', 'url',), extra=0, can_delete=True)
MainBannerFormset.deletion_widget = HiddenInput
NewsBannerFormset.deletion_widget = HiddenInput


class MainPageForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'MainPageModel')
        fields = ['phone1', 'phone2', 'seo_text', 'is_active']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            }),
            'seo_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
        }
        labels = {
            'phone1': '',
            'phone2': '',
            'seo_text': 'SEO текст',
        }


class ContactsPageForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'ContactsPageModel')
        fields = ['is_active']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            })
        }


class PageForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'PageModel')
        fields = ['title', 'description', 'banner', 'is_active']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            }),
            'title': forms.TextInput(attrs={
                'class': 'control-input'
            }),
            'banner': forms.FileInput()
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'banner': 'Главная картинка',
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'ContactModel')
        fields = ['title', 'address', 'coordinates', 'is_active', 'logo']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'coordinates': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            }),
            'logo': forms.FileInput()
        }
        labels = {
            'title': 'Название кинотеатра',
            'address': 'Адресс',
            'coordinates': 'Координаты для карты',
            'logo': 'Лого',
        }


ContactFormset = modelformset_factory(model=apps.get_model('cinema', 'ContactModel'), form=ContactForm,
                                      fields=('title', 'address', 'coordinates', 'is_active', 'logo'), extra=0,
                                      can_delete=True)
ContactFormset.deletion_widget = HiddenInput


class ArticleForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'ArticleModel')
        fields = ['title', 'description', 'banner', 'is_active', 'url', 'publication']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={
                'data-toggle': 'toggle',
                'data-onstyle': 'outline-success',
                'data-offstyle': 'outline-danger',
                'data-size': 'sm',
            }),
            'title': forms.TextInput(attrs={
                'class': 'control-input'
            }),
            'publication': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }),
            'banner': forms.FileInput()
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'banner': 'Главная картинка',
        }
