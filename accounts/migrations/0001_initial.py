# Generated by Django 3.0.5 on 2020-04-22 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_text', models.TextField(verbose_name='Введите текст публикации')),
                ('pub_pic', models.ImageField(null=True, upload_to='', verbose_name='Загрузите фото')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pub_likes', models.ManyToManyField(blank='True', related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='True', max_length=50, null=True)),
                ('phone', models.CharField(blank='True', max_length=50, null=True)),
                ('email', models.CharField(blank='True', max_length=50, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('subscribers', models.ManyToManyField(blank='True', related_name='subscribers', to=settings.AUTH_USER_MODEL)),
                ('subscriptions', models.ManyToManyField(blank='True', related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
                ('username', models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_from', models.CharField(blank=True, max_length=300, verbose_name='Другой пользователь')),
                ('notification_text', models.CharField(blank=True, max_length=300, verbose_name='Текст уведомления')),
                ('not_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата уведомления')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
