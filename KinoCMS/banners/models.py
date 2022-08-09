from django.db import models

from cinema.models import SEOModel, GalleryModel


class BannerConfigModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    active = models.BooleanField(verbose_name='Активно')
    rotation_speed = models.TimeField(verbose_name='Скорость перехода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Настройки баннеров'
        verbose_name = 'Настройки баннеров'
        ordering = ['pk']


class BackgroundBannerModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='background_banner_image',
                              verbose_name='Изображение')
    color = models.CharField(max_length=10, verbose_name='Цвет')
    is_image = models.BooleanField(verbose_name='Изображение')
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT, verbose_name='Настройки')

    def __str__(self):
        return "Фоновый баннер"

    class Meta:
        verbose_name_plural = 'Фоновые баннера'
        verbose_name = 'Фоновый баннер'
        ordering = ['pk']


class BannerMainPageModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_main_page_image',
                              verbose_name='Изображение')
    URL = models.URLField()
    text = models.CharField(max_length=50, verbose_name='Текст')

    def __str__(self):
        return "Баннер главной страницы"

    class Meta:
        verbose_name_plural = 'Баннер главной страницы'
        verbose_name = 'Баннер главной страницы'
        ordering = ['pk']


class BannerNewsPromoModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_new_promo_image',
                              verbose_name='Изображение')
    URL = models.URLField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT, verbose_name='Настройки')

    def __str__(self):
        return "Баннеры новостей и акций"

    class Meta:
        verbose_name_plural = 'Баннера новостей и промо'
        verbose_name = 'Баннер новостей и промо'
        ordering = ['pk']
