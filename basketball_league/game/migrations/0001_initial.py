# Generated by Django 5.0.1 on 2024-01-14 04:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Round",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Tounament",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="GamePlayerAssociation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField(default=0)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="game.game"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="players",
            field=models.ManyToManyField(
                through="game.GamePlayerAssociation", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="GameTeamAssociation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField(default=0)),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="game.game"
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="account.team"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="game",
            name="teams",
            field=models.ManyToManyField(
                through="game.GameTeamAssociation", to="account.team"
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="round",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="game.round"
            ),
        ),
        migrations.AddField(
            model_name="round",
            name="tournament",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="game.tounament",
            ),
        ),
    ]
