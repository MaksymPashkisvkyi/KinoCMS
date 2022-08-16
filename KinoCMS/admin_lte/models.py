from django.db import models


class SEOModel(models.Model):
    URL = models.URLField()
    title = models.CharField(max_length=50, verbose_name='Название')
    keywords = models.CharField(max_length=50, verbose_name='Ключевые слова')
    description = models.CharField(max_length=50, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'СЕО модели'
        verbose_name = 'СЕО модель'
        ordering = ['id']


class GalleryModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Галерея'
        verbose_name = 'Галерея'


class CinemaModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кинотеатр')
    description = models.TextField(verbose_name='Описание')
    condition = models.TextField(verbose_name='Условия')
    logo = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_logo', verbose_name='Лого')
    banner_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_banner_image',
                                     verbose_name='Баннер')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='cinema_gallery',
                                verbose_name='Галерея')
    seo_block = models.OneToOneField('SEOModel', on_delete=models.PROTECT, verbose_name='СЕО блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'
        ordering = ['name']


class HallModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    hall_scheme = models.FileField(verbose_name='Схема зала')
    cinema = models.ForeignKey('CinemaModel', on_delete=models.PROTECT, verbose_name='Кинотеатр')
    banner_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='hall_banner_image',
                                     verbose_name='Баннер')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='hall_gallery',
                                verbose_name='Галерея')
    seo_block = models.OneToOneField('SEOModel', on_delete=models.PROTECT, verbose_name='СЕО блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'
        ordering = ['name']


class FilmModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    main_image = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='film_main_image',
                                   verbose_name='Главное изображение')
    gallery = models.ForeignKey('GalleryModel', on_delete=models.PROTECT, related_name='film_gallery',
                                verbose_name='Галерея')
    URL = models.URLField()
    three_D = models.BooleanField(verbose_name='3D')
    two_D = models.BooleanField(verbose_name='2D')
    IMAX = models.BooleanField()
    seo_block = models.OneToOneField('SEOModel', on_delete=models.PROTECT, verbose_name='СЕО блок')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['name']


class SessionModel(models.Model):
    film = models.ForeignKey('FilmModel', on_delete=models.PROTECT, verbose_name='Фильм')
    hall = models.ForeignKey('HallModel', on_delete=models.PROTECT, verbose_name='Зал')
    price = models.SmallIntegerField(verbose_name='Стоимость')
    time = models.TimeField(verbose_name='Время')
    three_D = models.BooleanField(verbose_name='3D')
    DBOX = models.BooleanField()
    VIP = models.BooleanField()

    def __str__(self):
        return f"Сессия фильма {self.film}"

    class Meta:
        verbose_name_plural = 'Сессии'
        verbose_name = 'Сессия'


class TicketModel(models.Model):
    session = models.ForeignKey('SessionModel', on_delete=models.PROTECT, verbose_name='Сессия')
    user = models.ForeignKey('UserModel', on_delete=models.PROTECT, verbose_name='Пользователь')
    seat = models.SmallIntegerField(verbose_name='Место')
    reservation = models.BooleanField(verbose_name='Бронирование')

    def __str__(self):
        return f"Биллет {self.user}"

    class Meta:
        verbose_name_plural = 'Билеты'
        verbose_name = 'Билет'
        ordering = ['session']


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
