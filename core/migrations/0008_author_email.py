# Generated by Django 4.2.1 on 2023-05-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_author_detail_category_detail_post_detail_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
    ]
