# Generated by Django 5.0.2 on 2024-04-23 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.DateField(blank=True)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('interest', models.ManyToManyField(blank=True, to='group.interest')),
                ('like', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
