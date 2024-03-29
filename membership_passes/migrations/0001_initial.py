# Generated by Django 5.0.2 on 2024-03-04 17:47

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0004_alter_lessonmodel_duration_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity_lessons_max', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('is_unlimited', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('valid_from', models.DateField()),
                ('valid_until', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_passes', to='sections.sectionmodel')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_passes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('to_pass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='membership_passes.passmodel')),
            ],
        ),
    ]
