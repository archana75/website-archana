# Generated by Django 4.2.4 on 2023-10-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_event_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='school_product',
            field=models.BooleanField(default=False),
        ),
    ]
