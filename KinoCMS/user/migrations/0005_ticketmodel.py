# Generated by Django 4.1 on 2022-08-18 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_delete_ticketmodel'),
        ('user', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.SmallIntegerField(verbose_name='Место')),
                ('reservation', models.BooleanField(verbose_name='Бронирование')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.sessionmodel', verbose_name='Сессия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.usermodel', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'ordering': ['session'],
            },
        ),
    ]
