# Generated by Django 3.0 on 2021-04-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistroSocios', '0004_auto_20210413_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula',
            field=models.IntegerField(null=True),
        ),
    ]