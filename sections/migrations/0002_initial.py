# Generated by Django 5.0 on 2023-12-28 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmodel',
            name='students',
            field=models.ManyToManyField(related_name='my_groups', to='users.studentmodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='trainers',
            field=models.ManyToManyField(related_name='my_groups', to='users.trainermodel'),
        ),
        migrations.AddField(
            model_name='lessonmodel',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.groupmodel'),
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_own_section', to='users.trainermodel'),
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='students',
            field=models.ManyToManyField(related_name='section', to='users.studentmodel'),
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='trainers',
            field=models.ManyToManyField(related_name='section', to='users.trainermodel'),
        ),
        migrations.AddField(
            model_name='groupmodel',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='sections.sectionmodel'),
        ),
    ]