# Generated by Django 5.0 on 2023-12-19 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_verification', '0003_alter_confirmationcodemodel_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='confirmationcodemodel',
            unique_together=set(),
        ),
    ]
