# Generated by Django 3.2.7 on 2021-12-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20211106_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientName', models.CharField(max_length=200)),
                ('ClientDescription', models.CharField(max_length=200)),
            ],
        ),
    ]