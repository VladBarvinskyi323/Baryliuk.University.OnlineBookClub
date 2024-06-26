# Generated by Django 5.0.2 on 2024-04-03 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('user', '0002_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_user',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile_user',
            name='interest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='group.interest'),
        ),
    ]
