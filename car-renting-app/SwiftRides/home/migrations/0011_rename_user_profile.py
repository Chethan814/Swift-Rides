# Generated by Django 5.0.1 on 2024-03-26 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='profile',
        ),
    ]
