# Generated by Django 4.1.7 on 2023-05-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер'),
        ),
    ]