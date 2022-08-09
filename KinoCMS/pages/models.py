from django.db import models

from cinema.models import SEOModel, GalleryModel


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
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'
        ordering = ['name']


class ContactsModel(models.Model):
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
