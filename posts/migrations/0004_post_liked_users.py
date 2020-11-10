# Generated by Django 3.1.1 on 2020-11-03 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20201103_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
