# Generated by Django 3.1.4 on 2021-04-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='year',
            field=models.FloatField(),
        ),
    ]
