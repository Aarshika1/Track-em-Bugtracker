# Generated by Django 3.2.7 on 2021-09-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs_app', '0005_alter_bug_assigned_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assigned_user',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
