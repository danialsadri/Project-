# Generated by Django 4.2.10 on 2024-08-01 12:21

import apps.utils.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='آیدی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
                ('image', models.ImageField(upload_to=apps.utils.models.image_upload_to, verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]
