# Generated by Django 5.0.1 on 2024-03-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_alter_emailverification_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailverification",
            name="type",
            field=models.CharField(
                choices=[("PASS", "pass"), ("LOGIN", "login")],
                default="LOGIN",
                max_length=5,
            ),
        ),
    ]
