# Generated by Django 4.2.4 on 2024-02-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_achievement_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='thumbnail',
            field=models.ImageField(default=None, help_text='Ukuran foto 500x500 pixel', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='achievementphoto',
            name='photo',
            field=models.ImageField(help_text='maks size 4mb', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='attachment_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(help_text='maks size 4mb', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='maks size 4mb', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(help_text='maks size 4mb', upload_to='images'),
        ),
    ]