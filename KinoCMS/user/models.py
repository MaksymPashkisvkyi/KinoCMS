from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    nickname = models.CharField(max_length=50, verbose_name='Псевдоним')
    email = models.EmailField()
    address = models.CharField(max_length=50, verbose_name='Адресс')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    repeat_password = models.CharField(max_length=50, verbose_name='Повторить пароль')
    card_number = models.CharField(max_length=50, verbose_name='Номер карты')
    language = models.BooleanField(verbose_name='Язык')  # TODO Русский / Украинский?
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


class TicketModel(models.Model):
    session = models.ForeignKey('cinema.SessionModel', on_delete=models.PROTECT, verbose_name='Сессия')
    user = models.ForeignKey('UserModel', on_delete=models.PROTECT, verbose_name='Пользователь')
    seat = models.SmallIntegerField(verbose_name='Место')
    reservation = models.BooleanField(verbose_name='Бронирование')

    def __str__(self):
        return f"Биллет {self.user}"

    class Meta:
        verbose_name_plural = 'Билеты'
        verbose_name = 'Билет'
        ordering = ['session']
