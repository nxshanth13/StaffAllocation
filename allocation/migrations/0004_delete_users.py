# Generated by Django 4.1 on 2023-09-18 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]