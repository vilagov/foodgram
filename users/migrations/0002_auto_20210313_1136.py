# Generated by Django 3.1.6 on 2021-03-13 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]