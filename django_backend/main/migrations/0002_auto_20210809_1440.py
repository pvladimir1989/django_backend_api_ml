# Generated by Django 3.2.6 on 2021-08-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyofuseractions',
            options={'verbose_name': 'История транзацкий', 'verbose_name_plural': 'Истории транзацкий'},
        ),
        migrations.AlterModelOptions(
            name='mlmodels',
            options={'verbose_name': 'ML модель', 'verbose_name_plural': 'ML модели'},
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'Подписчик', 'verbose_name_plural': 'Подписчики'},
        ),
    ]
