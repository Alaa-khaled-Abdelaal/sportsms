# Generated by Django 4.2.1 on 2023-05-24 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_detail_images_detail_image_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='sport_icons'),
        ),
    ]
