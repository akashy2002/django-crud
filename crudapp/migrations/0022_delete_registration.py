# Generated by Django 4.1.7 on 2023-06-19 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0021_remove_registration_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
