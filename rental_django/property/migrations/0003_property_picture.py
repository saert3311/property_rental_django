# Generated by Django 5.0.6 on 2024-05-21 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_request_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='properties', verbose_name='Imagen'),
        ),
    ]
