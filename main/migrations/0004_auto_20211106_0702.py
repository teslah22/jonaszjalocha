# Generated by Django 3.2.7 on 2021-11-06 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_resume'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.RemoveField(
            model_name='postitem',
            name='postTitle',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
