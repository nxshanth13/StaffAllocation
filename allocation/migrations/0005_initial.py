# Generated by Django 4.1 on 2023-09-18 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('allocation', '0004_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2080)),
                ('department', models.CharField(max_length=2080)),
                ('email', models.CharField(max_length=2080)),
                ('password', models.CharField(max_length=2080)),
            ],
        ),
    ]
