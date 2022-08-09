from django.db import models


# from ..user.models import UserModel


class SEOModel(models.Model):
    URL = models.URLField()
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'СЕО модели'
        verbose_name = 'СЕО модель'


class GalleryModel(models.Model):
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class CinemaModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кинотеатр')
    description = models.TextField(verbose_name='Описание')
    condition = models.TextField(verbose_name='Условия')
    logo = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_logo', verbose_name='Лого')
    banner_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_banner_image',
                                     verbose_name='Баннер')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='cinema_gallery',
                                verbose_name='Галерея')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT, verbose_name='СЕО блок')

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'
        ordering = ['name']


class HallModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    hall_scheme = models.FileField()
    cinema = models.ForeignKey(CinemaModel, on_delete=models.PROTECT)
    banner_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='hall_banner_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='hall_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'
        ordering = ['name']


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

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['name']


class SessionModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.PROTECT)
    hall = models.ForeignKey(HallModel, on_delete=models.PROTECT)
    price = models.SmallIntegerField()
    time = models.TimeField()
    three_D = models.BooleanField()
    DBOX = models.BooleanField()
    VIP = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Сессии'
        verbose_name = 'Сессия'


class TicketModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.PROTECT)
    # user = models.ForeignKey(UserModel, on_delete=models.PROTECT) TODO ValueError: attempted relative import beyond top-level package
    seat = models.SmallIntegerField()
    reservation = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Билеты'
        verbose_name = 'Билет'
        ordering = ['session']


class MainPageModel(models.Model):
    first_phone = models.CharField(max_length=20)
    second_phone = models.CharField(max_length=20)
    seo_text = models.TextField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Главная страница'
        verbose_name = 'Главная страница'


class PagesModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='pages_main_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='pages_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Станицы'
        verbose_name = 'Страница'
        ordering = ['name']


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    coords = models.CharField(max_length=50)
    logo = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='contacts_logo')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'


class NewsPromoModel(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='news_promo_main_image')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='news_promo_gallery')
    URL = models.URLField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Новости и Промо'
        verbose_name = 'Новости и Промо'
        ordering = ['name']


class BannerConfigModel(models.Model):
    active = models.BooleanField()
    rotation_speed = models.TimeField()

    class Meta:
        verbose_name_plural = 'Настройки баннеров'
        verbose_name = 'Настройки баннеров'


class BackgroundBannerModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='background_banner_image')
    color = models.CharField(max_length=10)
    is_image = models.BooleanField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Фоновые баннера'
        verbose_name = 'Фоновый баннер'


class BannerMainPage(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_main_page_image')
    URL = models.URLField()
    text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Баннер главной страницы'
        verbose_name = 'Баннер главной страницы'


class BannerNewsPromo(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_new_promo_image')
    URL = models.URLField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Баннера новостей и промо'
        verbose_name = 'Баннер новостей и промо'
