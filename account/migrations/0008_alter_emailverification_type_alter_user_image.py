# Generated by Django 5.0.1 on 2024-03-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_emailverification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='type',
            field=models.CharField(choices=[('LOGIN', 'login'), ('PASS', 'pass')], default='LOGIN', max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/'),
        ),
    ]