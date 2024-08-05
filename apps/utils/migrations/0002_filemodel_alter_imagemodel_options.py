# Generated by Django 4.2.10 on 2024-08-05 17:53

import apps.utils.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='آیدی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
                ('file', models.FileField(upload_to=apps.utils.models.file_upload_to, verbose_name='فایل')),
            ],
            options={
                'verbose_name': 'فایل',
                'verbose_name_plural': 'فایل ها',
            },
        ),
        migrations.AlterModelOptions(
            name='imagemodel',
            options={'verbose_name': 'تصویر', 'verbose_name_plural': 'تصویر ها'},
        ),
    ]
