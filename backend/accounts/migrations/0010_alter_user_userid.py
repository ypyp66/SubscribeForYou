# Generated by Django 3.2.4 on 2021-06-23 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210624_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('[0-9a-z]+', 'only valid userid is required')], verbose_name='아이디'),
        ),
    ]