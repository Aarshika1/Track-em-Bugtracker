# Generated by Django 3.2.7 on 2021-09-28 10:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs_app', '0002_bug_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='assigned_user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
