# Generated by Django 5.0.1 on 2024-01-13 10:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('access_token', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('provider', models.CharField(default='google', max_length=50)),
                ('provider_id', models.CharField(max_length=50, unique=True)),
                ('image', models.URLField(null=True)),
                ('two_fact', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('EN', 'English'), ('KO', 'Korean'), ('ES', 'Spanish')], default='EN', max_length=2)),
            ],
            options={
                'db_table': 'app_user',
            },
        ),
    ]
