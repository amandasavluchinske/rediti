# Generated by Django 2.1.4 on 2019-01-13 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
