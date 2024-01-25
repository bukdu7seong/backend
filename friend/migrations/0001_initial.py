# Generated by Django 5.0.1 on 2024-01-18 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friends",
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
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("ACCEPTED", "Accepted")],
                        default="PENDING",
                        max_length=20,
                    ),
                ),
                (
                    "user1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friends_user1",
                        to="user.appuser",
                    ),
                ),
                (
                    "user2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="friends_user2",
                        to="user.appuser",
                    ),
                ),
            ],
            options={
                "db_table": "friends",
                "ordering": ["id"],
                "unique_together": {("user1", "user2")},
            },
        ),
    ]