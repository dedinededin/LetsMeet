from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    friends = models.ManyToManyField('self', blank=True)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return self.first_name + " " + self.last_name + " @" + self.user.username

    def fullname(self):
        return self.first_name + " " + self.last_name

    def requests(self):
        return FriendRequest.objects.filter(to_profile=self)

    def events(self):
        return Event.objects.filter(owner=EventOwner.objects.get(profile=self))

    def participated(self):
        return Event.objects.filter(participants=self).order_by('-time').reverse()


class FriendRequest(models.Model):
    from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

    def accept(self, user):
        user.profile.friends.add(self.from_profile)
        self.delete()

    def reject(self):
        self.delete()

    def __str__(self):
        return self.from_profile.user.username + ' to ' + self.to_profile.user.username


class EventOwner(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if self.profile:
            return self.profile.first_name + " " + self.profile.last_name


class Event(models.Model):
    time = models.DateTimeField()
    createdTime = models.DateTimeField(null=True)
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(EventOwner, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=150)
    participants = models.ManyToManyField(Profile, blank=True)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title + " @" + self.owner.profile.user.username
