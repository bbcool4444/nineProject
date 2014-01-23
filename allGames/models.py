from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
        return '%s(%s)' % (user, pub_date)

class Reply(models.Model):
    user = models.CharField(max_length=10)
    recomment = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return '%s(%s)' % (self.user, self.pub_date)

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

class RecommendComment(models.Model):
    user = models.CharField(max_length=10)
    game = models.ForeignKey(Recommend)
    comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return '%s(%s)' % (user, pub_date)

class RecommendReply(models.Model):
    user = models.CharField(max_length=10)
    recomment = models.CharField(max_length=200)
    comment = models.ForeignKey(RecommendComment)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return '%s(%s)' % (self.user, self.pub_date)


####################################### user model #########################################

class UserProfile(models.Model):
    '''
    user information
    '''
    user = models.OneToOneField(User)
    uid = models.IntegerField(u'uid', unique=True, default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def __unicode__(self):
        return self.user

####################################### /user model #########################################
