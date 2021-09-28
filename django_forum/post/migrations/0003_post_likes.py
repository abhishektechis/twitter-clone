# Generated by Django 3.2.7 on 2021-09-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
    ]
