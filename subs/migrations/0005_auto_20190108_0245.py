# Generated by Django 2.1.4 on 2019-01-08 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0004_subrediti_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created']},
        ),
    ]
