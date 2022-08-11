# Generated by Django 4.1 on 2022-08-11 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_hallmodel_banner_image_alter_hallmodel_cinema_and_more'),
        ('pages', '0002_alter_contactsmodel_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название кинотеатра')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('coords', models.CharField(max_length=50, verbose_name='Координаты')),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contacts_logo', to='cinema.gallerymodel', verbose_name='Лого')),
                ('seo_block', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel', verbose_name='СЕО блок')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='PageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages_gallery', to='cinema.gallerymodel', verbose_name='Галерея')),
                ('main_image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages_main_image', to='cinema.gallerymodel', verbose_name='Главное изображение страницы')),
                ('seo_block', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cinema.seomodel', verbose_name='СЕО блок')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='pagesmodel',
            name='seo_block',
        ),
        migrations.DeleteModel(
            name='ContactsModel',
        ),
        migrations.DeleteModel(
            name='PagesModel',
        ),
    ]
