# Generated by Django 5.0.1 on 2024-01-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_appuser_created_at_alter_appuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted')], default='PENDING', max_length=20),
        ),
    ]