# Generated by Django 4.2.10 on 2024-08-01 12:21

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='آیدی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='ویرایش شده در')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام کاربری')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='کد ملی')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خانوادگی')),
                ('photo', models.ImageField(blank=True, default='photo/photo.png', null=True, upload_to='photo/', verbose_name='تصویر')),
                ('login_time', models.DateTimeField(blank=True, null=True, verbose_name='آخرین ورود')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='ادمین')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='ابرکاربر')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['-created_at'], name='accounts_us_created_d650d4_idx')],
            },
        ),
    ]
