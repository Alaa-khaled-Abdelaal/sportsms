# Generated by Django 4.2.1 on 2023-06-07 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_rename_image_detail_image1_detail_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='image1',
            new_name='image',
        ),
    ]
