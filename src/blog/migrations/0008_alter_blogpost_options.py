# Generated by Django 4.2.1 on 2023-05-29 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_publish_date_blogpost_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
