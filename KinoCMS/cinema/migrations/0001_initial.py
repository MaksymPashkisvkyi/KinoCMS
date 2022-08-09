# Generated by Django 4.1 on 2022-08-08 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SEOModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CinemaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('condition', models.TextField()),
                ('banner_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='banner_image_gallery', to='cinema.gallerymodel')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gallery_gallery', to='cinema.gallerymodel')),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='logo_gallery', to='cinema.gallerymodel')),
                ('seo_block', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel')),
            ],
        ),
    ]
