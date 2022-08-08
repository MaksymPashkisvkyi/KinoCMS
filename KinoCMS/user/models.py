from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    repeat_password = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    language = models.BooleanField()
    gender = models.BooleanField()
    phone = models.CharField()
    data = models.DateField()
    # city = models.ChoiceField() TODO ChoiceField?