# Generated by Django 4.1 on 2022-08-09 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Кинотеатр')),
                ('description', models.TextField(verbose_name='Описание')),
                ('condition', models.TextField(verbose_name='Условия')),
            ],
            options={
                'verbose_name': 'Кинотеатр',
                'verbose_name_plural': 'Кинотеатры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FilmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('URL', models.URLField()),
                ('three_D', models.BooleanField()),
                ('two_D', models.BooleanField()),
                ('IMAX', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='HallModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('hall_scheme', models.FileField(upload_to='')),
                ('banner_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hall_banner_image', to='cinema.gallerymodel')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.cinemamodel')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hall_gallery', to='cinema.gallerymodel')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
                'ordering': ['name'],
            },
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
            options={
                'verbose_name': 'СЕО модель',
                'verbose_name_plural': 'СЕО модели',
            },
        ),
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.SmallIntegerField()),
                ('time', models.TimeField()),
                ('three_D', models.BooleanField()),
                ('DBOX', models.BooleanField()),
                ('VIP', models.BooleanField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.filmmodel')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.hallmodel')),
            ],
            options={
                'verbose_name': 'Сессия',
                'verbose_name_plural': 'Сессии',
            },
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.SmallIntegerField()),
                ('reservation', models.BooleanField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.sessionmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.usermodel')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'ordering': ['session'],
            },
        ),
        migrations.AddField(
            model_name='hallmodel',
            name='seo_block',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel'),
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='film_gallery', to='cinema.gallerymodel'),
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='main_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='film_main_image', to='cinema.gallerymodel'),
        ),
        migrations.AddField(
            model_name='filmmodel',
            name='seo_block',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel'),
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='banner_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cinema_banner_image', to='cinema.gallerymodel', verbose_name='Баннер'),
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cinema_gallery', to='cinema.gallerymodel', verbose_name='Галерея'),
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='logo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cinema_logo', to='cinema.gallerymodel', verbose_name='Лого'),
        ),
        migrations.AddField(
            model_name='cinemamodel',
            name='seo_block',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel', verbose_name='СЕО блок'),
        ),
    ]
