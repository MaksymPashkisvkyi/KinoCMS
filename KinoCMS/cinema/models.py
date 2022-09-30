import os

from colorfield.fields import ColorField
from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class SeoModel(models.Model):
    seo_url = models.URLField()
    seo_title = models.CharField(max_length=50)
    seo_keywords = models.CharField(max_length=100)
    seo_description = models.TextField()

    def __str__(self):
        return self.seo_title


class GalleryModel(models.Model):
    title = models.CharField(max_length=50)


class ImageModel(models.Model):
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'gallery'))
    url = models.URLField()
    text = models.CharField(max_length=50)


class CinemaModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    condition = models.TextField()
    logo = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'cinemas', 'logo'))
    banner = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'cinemas', 'banners'))
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class HallModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    hall_scheme = models.FileField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'halls', 'hall_schemes'))
    banner = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'halls', 'banners'))
    cinema = models.ForeignKey('CinemaModel', on_delete=models.CASCADE, null=True)
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class FilmModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField()
    is_active = models.BooleanField()
    is_2d = models.BooleanField()
    is_3d = models.BooleanField()
    is_imax = models.BooleanField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'films', 'banners'))
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class SeanceModel(models.Model):
    price = models.SmallIntegerField()
    time = models.TimeField()
    is_3d = models.BooleanField()
    is_dbox = models.BooleanField()
    is_vip = models.BooleanField()
    film = models.ForeignKey('FilmModel', on_delete=models.CASCADE)
    hall = models.ForeignKey('HallModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Сессия фильма {self.film}"


class TicketModel(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    is_reservation = models.BooleanField()
    client = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)
    seance = models.ForeignKey('SeanceModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Биллет {self.client}"


class MainPageModel(models.Model):
    title = models.CharField(max_length=50, default='Main')
    is_active = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    phone1 = PhoneNumberField(blank=True, null=True)
    phone2 = PhoneNumberField(blank=True, null=True)
    seo_text = models.TextField(null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE, null=True)


class PageModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'pages', 'banners'), null=True)
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ContactsPageModel(models.Model):
    title = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE, null=True)


class ContactModel(models.Model):
    contacts_page = models.ForeignKey('ContactsPageModel', on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    coordinates = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    logo = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'contacts', 'logos'))

    def __str__(self):
        return self.title


class ArticleModel(models.Model):
    class Mode(models.TextChoices):
        NEWS = 'NEWS'
        PROMO = 'PROMO'

    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    url = models.URLField()
    publication = models.DateField(db_index=True)
    mode = models.CharField(max_length=10, choices=Mode.choices)
    banner = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'articles', 'banners'))
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    seo = models.OneToOneField('SeoModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BackgroundBannerModel(models.Model):
    mode = models.CharField(max_length=20, choices=[('Фото на фоне', 'Фото на фоне'), ("Просто фон", "Просто фон")],
                            default="Просто фон")
    image = models.ImageField(upload_to=os.path.join(MEDIA_ROOT, 'images', 'banners', 'background'), null=True,
                              default=None)
    color = ColorField()


class BannerModel(models.Model):
    name = models.CharField(max_length=40, unique=True)
    gallery = models.ForeignKey('GalleryModel', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)
    rotation_speed = models.PositiveSmallIntegerField(null=True)
