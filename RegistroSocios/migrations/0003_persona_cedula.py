# Generated by Django 3.0 on 2021-04-13 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RegistroSocios', '0002_auto_20210410_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='cedula',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]