# Generated by Django 2.1.4 on 2019-01-08 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0003_auto_20181230_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='subrediti',
            name='slug',
            field=models.SlugField(default='sub'),
            preserve_default=False,
        ),
    ]
