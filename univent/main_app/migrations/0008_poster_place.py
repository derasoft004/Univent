# Generated by Django 5.1.2 on 2024-10-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_merge_20241026_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='place',
            field=models.CharField(default='place', max_length=255),
            preserve_default=False,
        ),
    ]