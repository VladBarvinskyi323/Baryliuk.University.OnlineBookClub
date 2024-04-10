# Generated by Django 5.0.2 on 2024-04-03 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('interest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='group.interest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]