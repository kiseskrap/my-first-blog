# Generated by Django 4.1.8 on 2023-05-04 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titile',
            new_name='title',
        ),
    ]
