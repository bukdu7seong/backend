# Generated by Django 5.0.1 on 2024-02-01 07:52

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="username"
                    ),
                ),
                ("intraId", models.CharField(default="", max_length=20, unique=True)),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email"
                    ),
                ),
                ("password", models.CharField(max_length=20, verbose_name="password")),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("twoFactor", models.BooleanField(default=True)),
                (
                    "language",
                    models.CharField(
                        choices=[("EN", "English"), ("FR", "French"), ("KR", "Korean")],
                        default="KR",
                        max_length=4,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "user",
            },
            managers=[
                ("objects", account.models.UserManager()),
            ],
        ),
    ]
