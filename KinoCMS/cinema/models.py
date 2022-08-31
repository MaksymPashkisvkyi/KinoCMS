from django.db import models


class SEOModel(models.Model):
    URL = models.URLField()
    title = models.CharField(max_length=50, verbose_name='Название')
    keywords = models.CharField(max_length=50, verbose_name='Ключевые слова')
    description = models.CharField(max_length=50, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'SEO модели'
        verbose_name = 'SEO модель'
        ordering = ['id']


class GalleryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class CinemaModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название кинотеатра')
    description = models.TextField(verbose_name='Описание')
    condition = models.TextField(verbose_name='Условия')
    logo = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_logo',
                             verbose_name='Логотип')
    banner_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_banner_image',
                                     verbose_name='Фото верхнего баннера')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_gallery',
                                verbose_name='Галерея картинок')
    seo_block = models.OneToOneField('SEOModel', blank=True, on_delete=models.CASCADE, verbose_name='SEO блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'
        ordering = ['name']


class HallModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Номер зала')
    description = models.TextField(verbose_name='Описание зала')
    hall_scheme = models.FileField(verbose_name='Схема зала', blank=True)
    cinema = models.ForeignKey('CinemaModel', on_delete=models.CASCADE, verbose_name='Кинотеатр')
    banner_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='hall_banner_image',
                                     verbose_name='Верхний баннер')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='hall_gallery',
                                verbose_name='Галерея картинок')
    seo_block = models.OneToOneField('SEOModel', blank=True, on_delete=models.PROTECT, verbose_name='SEO блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'
        ordering = ['name']


class FilmModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    main_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='film_main_image',
                                   verbose_name='Главное изображение')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='film_gallery',
                                verbose_name='Галерея')
    URL = models.URLField()
    three_D = models.BooleanField(verbose_name='3D')
    two_D = models.BooleanField(verbose_name='2D')
    IMAX = models.BooleanField()
    seo_block = models.OneToOneField('SEOModel', blank=True, on_delete=models.PROTECT, verbose_name='SEO блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['name']


class SessionModel(models.Model):
    film = models.ForeignKey('FilmModel', on_delete=models.PROTECT, verbose_name='Фильм')
    hall = models.ForeignKey('HallModel', on_delete=models.PROTECT, verbose_name='Зал')
    price = models.SmallIntegerField(verbose_name='Стоимость')
    time = models.TimeField(verbose_name='Время')
    three_D = models.BooleanField(verbose_name='3D')
    DBOX = models.BooleanField()
    VIP = models.BooleanField()

    def __str__(self):
        return f"Сессия фильма {self.film}"

    class Meta:
        verbose_name_plural = 'Сессии'
        verbose_name = 'Сессия'
