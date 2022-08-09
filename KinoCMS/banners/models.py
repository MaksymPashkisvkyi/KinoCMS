from django.db import models

from cinema.models import SEOModel, GalleryModel


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


class BannerMainPageModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_main_page_image')
    URL = models.URLField()
    text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Баннер главной страницы'
        verbose_name = 'Баннер главной страницы'


class BannerNewsPromoModel(models.Model):
    image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_new_promo_image')
    URL = models.URLField()
    config = models.OneToOneField(BannerConfigModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Баннера новостей и промо'
        verbose_name = 'Баннер новостей и промо'
