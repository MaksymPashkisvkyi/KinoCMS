from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    nickname = models.CharField(max_length=50, verbose_name='Ник')
    email = models.EmailField()
    address = models.CharField(max_length=50, verbose_name='Адрес')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    repeat_password = models.CharField(max_length=50, verbose_name='Повторить пароль')
    card_number = models.CharField(max_length=50, verbose_name='Номер карты')
    language = models.BooleanField(verbose_name='Язык') # Русский / Украинский?
    gender = models.BooleanField(verbose_name='Пол')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    date = models.DateField(verbose_name='Дата рождения')
    city = models.CharField(max_length=50, verbose_name='Город')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['name']
