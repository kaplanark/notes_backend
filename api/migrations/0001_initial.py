# Generated by Django 4.1 on 2022-08-23 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField()),
                ('title', models.CharField(max_length=5000)),
                ('text', models.CharField(max_length=15000)),
                ('color', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=500)),
                ('show', models.BooleanField()),
                ('pinned', models.BooleanField()),
                ('archived', models.BooleanField()),
                ('trashed', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
