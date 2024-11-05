# Generated by Django 5.1.2 on 2024-11-05 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('creator', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, null=True)),
                ('price', models.IntegerField()),
                ('short_description', models.TextField(blank=True, null=True)),
                ('full_description', models.TextField(blank=True, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_event', models.DateTimeField()),
                ('preview_image', models.CharField(blank=True, max_length=255, null=True)),
                ('background_image', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True)),
                ('nickname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('hobby', models.TextField(blank=True, null=True)),
                ('is_creator', models.BooleanField(default=False)),
                ('events', models.ManyToManyField(related_name='poster', to='main_app.poster')),
            ],
        ),
        migrations.AddField(
            model_name='poster',
            name='subscribers',
            field=models.ManyToManyField(related_name='user', to='main_app.user'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('call_time', models.DateTimeField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender', to='main_app.user')),
            ],
        ),
    ]
