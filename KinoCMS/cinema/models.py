from django.db import models
# from ..user.models import UserModel


class SEOModel(models.Model):
    URL = models.URLField()
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class GalleryModel(models.Model):
    image = models.ImageField()


class CinemaModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    condition = models.TextField()
    logo = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_logo')
    banner_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_banner_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class HallModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    hall_scheme = models.FileField()
    cinema = models.ForeignKey(CinemaModel, on_delete=models.PROTECT)
    banner_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='hall_banner_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='hall_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class FilmModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='film_main_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='film_gallery')
    URL = models.URLField()
    three_D = models.BooleanField()
    two_D = models.BooleanField()
    IMAX = models.BooleanField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class SessionModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.PROTECT)
    hall = models.ForeignKey(HallModel, on_delete=models.PROTECT)
    price = models.SmallIntegerField()
    time = models.TimeField()
    three_D = models.BooleanField()
    DBOX = models.BooleanField()
    VIP = models.BooleanField()


class TicketModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.PROTECT)
    # user = models.ForeignKey(UserModel, on_delete=models.PROTECT) TODO ValueError: attempted relative import beyond top-level package
    seat = models.SmallIntegerField()
    reservation = models.BooleanField()


class MainPageModel(models.Model):
    first_phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20)
    seo_text = models.TextField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class PagesModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='pages_main_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='pages_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    coords = models.CharField(max_length=50)
    logo = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='contacts_logo')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class NewsPromoModel(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='news_promo_main_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='news_promo_gallery')
    URL = models.URLField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)


class BannerConfigModel(models.Model):
    active = models.BooleanField()
    rotation_speed = models.TimeField()


class BackgroundBannerModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='background_banner_image')
    color = models.CharField(max_length=10)
    is_image = models.BooleanField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT)


class BannerMainPage(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_main_page_image')
    URL = models.URLField()
    text = models.CharField(max_length=50)


class BannerNewsPromo(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_new_promo_image')
    URL = models.URLField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT)
