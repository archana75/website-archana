# Generated by Django 4.2.4 on 2023-11-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_cms_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
