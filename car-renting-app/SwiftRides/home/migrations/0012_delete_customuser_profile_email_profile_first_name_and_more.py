# Generated by Django 5.0.1 on 2024-03-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
