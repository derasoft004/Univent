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

