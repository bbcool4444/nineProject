from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='allGames', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=35)
    image = models.ImageField(upload_to='allGames', null=True, blank=True)

    def __unicode__(self):
        return self.name
