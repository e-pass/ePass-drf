# Generated by Django 5.0 on 2024-03-04 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership_passes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passmodel',
            name='qr_code',
        ),
    ]
