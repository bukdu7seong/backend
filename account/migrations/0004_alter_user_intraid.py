# Generated by Django 5.0.1 on 2024-02-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_user_groups_user_is_superuser_user_user_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="intraId",
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]