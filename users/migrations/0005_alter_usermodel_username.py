# Generated by Django 4.2.7 on 2023-11-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_usermodel_is_phone_number_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
