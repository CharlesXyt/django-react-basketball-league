# Generated by Django 5.0.1 on 2024-01-14 05:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("game", "0002_game_name"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tounament",
            new_name="Tournament",
        ),
    ]
