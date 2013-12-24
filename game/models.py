from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='game', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='game', null=True, blank=True)

    def __unicode__(self):
        return self.title
