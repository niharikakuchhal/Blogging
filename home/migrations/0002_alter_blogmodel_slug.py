# Generated by Django 5.0.6 on 2024-06-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogmodel",
            name="slug",
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
