# Generated by Django 5.0.1 on 2024-01-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="name",
            field=models.CharField(default="", max_length=255),
        ),
    ]
