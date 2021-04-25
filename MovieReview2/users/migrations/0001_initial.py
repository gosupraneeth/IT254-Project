# Generated by Django 3.1.4 on 2021-04-24 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('mid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('year', models.FloatField()),
                ('duration', models.FloatField()),
                ('director', models.CharField(max_length=150)),
                ('writer', models.CharField(max_length=150)),
                ('production', models.CharField(max_length=200)),
                ('actors', models.TextField()),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PriorityLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plname', models.CharField(max_length=64)),
                ('plval', models.IntegerField()),
                ('users', models.ManyToManyField(blank=True, related_name='language', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='PriorityGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgname', models.CharField(max_length=64)),
                ('pgval', models.IntegerField()),
                ('users', models.ManyToManyField(blank=True, related_name='genre', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_name', models.CharField(max_length=64)),
                ('movies', models.ManyToManyField(blank=True, related_name='language', to='users.Movies')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=64)),
                ('movies', models.ManyToManyField(blank=True, related_name='genre', to='users.Movies')),
            ],
        ),
    ]
