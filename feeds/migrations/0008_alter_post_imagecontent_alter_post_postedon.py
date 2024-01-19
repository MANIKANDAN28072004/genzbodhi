# Generated by Django 4.2.3 on 2023-07-17 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_alter_post_imagecontent_alter_post_postedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageContent',
            field=models.ImageField(null=True, upload_to='post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postedOn',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 17, 21, 35, 5, 39950)),
        ),
    ]
