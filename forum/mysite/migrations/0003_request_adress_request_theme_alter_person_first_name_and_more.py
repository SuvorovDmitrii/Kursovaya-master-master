# Generated by Django 4.1.7 on 2023-05-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_person_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='adress',
            field=models.CharField(default=1, max_length=200, verbose_name='Адресс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='theme',
            field=models.CharField(default=1, max_length=50, verbose_name='Тема запроса'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]