from django.db import models

from user.models import UserModel


class SEOModel(models.Model):
    URL = models.URLField()
    title = models.CharField(max_length=50, verbose_name='Название')
    keywords = models.CharField(max_length=50, verbose_name='Ключевые слова')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'СЕО модели'
        verbose_name = 'СЕО модель'


class GalleryModel(models.Model):
    image = models.ImageField(verbose_name='Изображение')

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
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    main_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='film_main_image',
                                   verbose_name='Главное изображение')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='film_gallery',
                                verbose_name='Галерея')
    URL = models.URLField()
    three_D = models.BooleanField(verbose_name='3D')
    two_D = models.BooleanField(verbose_name='2D')
    IMAX = models.BooleanField()
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT, verbose_name='СЕО блок')

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['name']


class SessionModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.PROTECT, verbose_name='Фильм')
    hall = models.ForeignKey(HallModel, on_delete=models.PROTECT, verbose_name='Зал')
    price = models.SmallIntegerField(verbose_name='Стоимость')
    time = models.TimeField(verbose_name='Время')
    three_D = models.BooleanField(verbose_name='3D')
    DBOX = models.BooleanField()
    VIP = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Сессии'
        verbose_name = 'Сессия'


class TicketModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.PROTECT, verbose_name='Сессия')
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, verbose_name='Пользователь')
    seat = models.SmallIntegerField(verbose_name='Место')
    reservation = models.BooleanField(verbose_name='Бронирование')

    class Meta:
        verbose_name_plural = 'Билеты'
        verbose_name = 'Билет'
        ordering = ['session']
