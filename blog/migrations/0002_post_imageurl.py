# Generated by Django 5.1.11 on 2025-07-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageUrl',
            field=models.TextField(blank=True, null=True),
        ),
    ]
