from django import forms
from django.apps import apps


class AddCinemaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo'].empty_label = 'Логотип не выбран'
        self.fields['banner_image'].empty_label = 'Фото верхнего баннера не выбрано'
        self.fields['seo_block'].empty_label = 'SEO блок не выбран'

    class Meta:
        model = apps.get_model('cinema', 'CinemaModel')
        fields = ['name', 'description', 'condition', 'logo', 'banner_image', 'gallery', 'seo_block']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'condition': forms.Textarea(attrs={'rows': 5})
        }


class AddHallForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cinema'].empty_label = 'Кинотеатр не выбран'
        self.fields['banner_image'].empty_label = 'Фото верхнего баннера не выбрано'
        self.fields['seo_block'].empty_label = 'SEO блок не выбран'

    class Meta:
        model = apps.get_model('cinema', 'HallModel')
        fields = ['name', 'description', 'hall_scheme', 'cinema', 'banner_image', 'gallery', 'seo_block']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'rows': 5})
        }


class AddSEOForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'SEOModel')
        fields = ['URL', 'title', 'keywords', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'keywords': forms.Textarea(attrs={'rows': 5}),
            'description': forms.Textarea(attrs={'rows': 5})
        }


class AddGalleryForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'GalleryModel')
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'})
        }


class AddUserForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('user', 'UserModel')
        fields = ['name', 'surname', 'nickname', 'email', 'address', 'password', 'repeat_password', 'card_number',
                  'language', 'gender', 'phone', 'date', 'city']


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('cinema', 'FilmModel')
        fields = ['name', 'description', 'main_image', 'gallery', 'URL', 'three_D', 'two_D', 'IMAX', 'seo_block']
