# Generated by Django 4.2.4 on 2023-10-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_cms_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
