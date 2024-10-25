from django.db import models


class Poster(models.Model):
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_event = models.DateTimeField()
    preview_image = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.creator}_{self.title}'


class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    is_creator = models.BooleanField(default=False)
    events = models.ManyToManyField('Poster', related_name='poster')

    def __str__(self):
        return self.nickname