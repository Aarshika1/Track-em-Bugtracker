# Generated by Django 3.2.7 on 2021-09-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sector',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
