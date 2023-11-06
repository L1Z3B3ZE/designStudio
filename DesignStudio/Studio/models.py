from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from datetime import datetime


class AdvUser(AbstractUser):
   name = models.CharField(max_length=250, verbose_name="ФИО", help_text="Только кириллические буквы, дефис и пробелы")
   username = models.CharField(max_length=35, verbose_name="Логин", unique=True, help_text="Только латиница и дефис, уникальный")
   is_activated = models.BooleanField(default=True, db_index=True,
                                      verbose_name='Согласие с правилами регистрации')

class Meta(AbstractUser.Meta):
   pass




class Application(models.Model):
    application_title = models.CharField(max_length=254, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    REQUEST_CATEGORY = (
        ('bigApartment', 'bigApartment'),
        ('mediumApartment', 'mediumApartment'),
        ('smallApartment', 'smallApartment'),
    )
    category = models.CharField(
        max_length=15,
        choices=REQUEST_CATEGORY,
        blank=True,
        default='a',
        verbose_name="Категория")

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit  * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    photo_of_room = models.ImageField(max_length=254, upload_to="media/", verbose_name="Фотография",
                                      help_text="Разрешается формата файла только jpg, jpeg, png, bmp",
                                      validators=[
                                          FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']),
                                        validate_image])
    date_create = models.DateField(default=datetime.now, verbose_name="Дата создания")
    time_create = models.TimeField(default=datetime.now, verbose_name="Время создания")
    REQUEST_STATUS = (
        ('Новая', 'Новая'),
        ('Принято в работу', 'Принято в работу'),
        ('Выполнено', 'Выполнено'),
    )
    status = models.CharField(
        max_length=16,
        choices=REQUEST_STATUS,
        default='Новая',
        blank=True,
        verbose_name="Статус")
    owner = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.application_title


