# Generated by Django 4.2.4 on 2024-03-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_program_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='programphoto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]