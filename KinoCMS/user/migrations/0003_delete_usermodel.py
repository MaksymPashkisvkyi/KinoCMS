# Generated by Django 4.1 on 2022-08-16 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_remove_filmmodel_gallery_remove_filmmodel_main_image_and_more'),
        ('user', '0002_alter_usermodel_address_alter_usermodel_card_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
