# Generated by Django 2.2 on 2020-06-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200612_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='resistors',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='blog/img'),
        ),
        migrations.AddField(
            model_name='resistors',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='blog/img'),
        ),
        migrations.AddField(
            model_name='resistors',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='blog/img'),
        ),
        migrations.AddField(
            model_name='resistors',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='blog/img'),
        ),
    ]
