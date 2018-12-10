from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " @" + self.user.username


class EventOwner(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.profile:
            return self.profile.first_name + " " + self.profile.last_name


class Event(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(EventOwner, on_delete=models.CASCADE, null=True)
    participants = models.ManyToManyField(Profile, blank=True)
    description = models.CharField(max_length=500, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title
