# Generated by Django 3.2.7 on 2021-09-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0002_project_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
