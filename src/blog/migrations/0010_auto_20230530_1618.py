# Generated by Django 2.2 on 2023-05-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
