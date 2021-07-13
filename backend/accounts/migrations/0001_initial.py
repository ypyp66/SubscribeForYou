# Generated by Django 3.2.4 on 2021-07-12 13:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-z]{1}[0-9a-z]+$', 'only valid userid is required')], verbose_name='아이디')),
                ('password', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^.*(?=^.{8,15}$)(?=.*\\d)(?=.*[a-zA-Z])(?=.*[^a-zA-Z0-9]).*$', 'only valid password is required')], verbose_name='비밀번호')),
                ('u_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[가-힣]+$', 'only valid name is required')], verbose_name='이름')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='이메일')),
                ('gender', models.CharField(max_length=10, verbose_name='성별')),
                ('birth_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)], verbose_name='출생년도')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
