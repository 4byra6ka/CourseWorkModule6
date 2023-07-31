# Generated by Django 4.2.3 on 2023-07-14 14:15

import datetime
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
            name='MailingClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_email', models.EmailField(max_length=254, verbose_name='контактный email')),
                ('fio', models.CharField(max_length=100, verbose_name='фио')),
                ('comment', models.TextField(verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_subject', models.CharField(verbose_name='тема письма')),
                ('email_body', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_time', models.TimeField(default=datetime.datetime(2023, 7, 14, 17, 15, 35, 853925), verbose_name='время рассылки')),
                ('intervals', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], verbose_name='периодичность')),
                ('status_mailing', models.CharField(choices=[('created', 'Создана'), ('running', 'Запущена'), ('completed', 'Завершена')], verbose_name='статус рассылки')),
                ('mailing_client', models.ManyToManyField(to='skysend.mailingclient')),
                ('mailing_message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skysend.mailingmessage')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Настройка рассылка',
                'verbose_name_plural': 'Настройки рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_time_status', models.DateTimeField(verbose_name='дата и время последней попытки')),
                ('attempted_status', models.BooleanField(verbose_name='статус попытки')),
                ('mail_server_response', models.TextField(verbose_name='ответ почтового сервера')),
                ('mailing_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skysend.mailingsettings')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
    ]
