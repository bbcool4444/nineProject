from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='allGames', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    user = models.CharField(max_length=10)
    game = models.ForeignKey(Game)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return '%s(%s)' % (self.game.name, self.user)

class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    descriptions = models.CharField(max_length=35)
    image = models.ImageField(upload_to='allGames', null=True, blank=True)

    def __unicode__(self):
        return self.name

class Recommend(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to='allGames', null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name
