from django.db import models


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
    logo = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='logo_gallery')
    banner_image = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='banner_image_gallery')
    gallery = models.ForeignKey(GalleryModel, on_delete=models.PROTECT, related_name='gallery_gallery')
    seo_block = models.OneToOneField(SEOModel, on_delete=models.PROTECT)
