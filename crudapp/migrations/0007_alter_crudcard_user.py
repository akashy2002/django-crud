# Generated by Django 4.1.7 on 2023-06-10 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crudcard',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.registration'),
        ),
    ]
