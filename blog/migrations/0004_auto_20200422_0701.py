# Generated by Django 3.0.5 on 2020-04-22 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200413_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
    ]
