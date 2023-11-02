# Generated by Django 4.2.5 on 2023-11-02 06:52

import Studio.models
import datetime
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_title', models.CharField(max_length=254, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('category', models.CharField(blank=True, choices=[('bigApartment', 'bigApartment'), ('Apartment', 'bigApartment'), ('smallApartment', 'smallApartment')], default='a', max_length=14, verbose_name='Категория')),
                ('photo_of_room', models.ImageField(help_text='Разрешается формата файла только jpg, jpeg, png, bmp', max_length=254, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), Studio.models.Application.validate_image], verbose_name='Фотография')),
                ('time_create', models.TimeField(default=datetime.datetime(2023, 11, 2, 13, 52, 0, 147966), verbose_name='Время создания')),
                ('status', models.CharField(blank=True, choices=[('Новая', 'Новая'), ('Принято в работу', 'Принято в работу'), ('«Выполнено»', '«Выполнено»')], default='Новая', max_length=16, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(help_text='Только кириллические буквы, дефис и пробелы', max_length=250, verbose_name='ФИО')),
                ('username', models.CharField(help_text='Только латиница и дефис, уникальный', max_length=35, unique=True, verbose_name='Логин')),
                ('is_activated', models.BooleanField(db_index=True, default=True, verbose_name='Согласие с правилами регистрации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
