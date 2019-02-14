# LetsMeet
Let's Meet is a social web site which aims to organize events easier. This project is an assignment for Sofware Engineering Concepts lecture.


![](https://lh6.googleusercontent.com/ofuWr7rtq0wufSLp17sfTc4CX3Ubh8dNCvJYLlb6BEWHBIOrNME5uMgdV9NnLYRiPDPQ4obRuYTs3Otf6yBzdsJdn6QHpYQ_Bbf6bfGlUVEn8idkVrkBlqGcPcc6OGYVmT-_q190)

----------

![](https://lh4.googleusercontent.com/M5gsYC6xSD4R9IM9H-Wy04pFLA8I79Z-HcK54D7xT9TCfpkpvWYNu43WBUd_Za9sxk_DJ5FG6nIDC09oG6WJ5loEySWw2CEz5mP_zlhPVjiinrkvRl_zKIBIWm7lVkdD5ve5kin5)

----------

![](https://lh5.googleusercontent.com/juZhuV9X8qFtmGkZ7GO_yZXaskIdUchNNCjF4l9m5DZtKDaMIgeCRIb3f2jpj9BeiiOHO2G9mYOFBz2QWh73fYDkdxLsWFzGd1su_vgIlLf0T8FnArMi_LAm4sc-Woamxz_yr58i)

Prepared by:

İbrahim Doğan - 11512112

Burak Demirel - 115200034

Engin Can Höke - 116202067

Recep Goger - 114200078

Kadir Akgül - 115200081

  

Semester: Fall 2018

  

Course: Software Engineering Consepts

  

Instructed by Pınar Hacıbeyoğlu

![](https://lh5.googleusercontent.com/fi5dhx0gZg9YgUoRdwCV-FiJX0dh8TzmkbwGrZIRhIWUjyN14F3mFPo9yfBZSqf7Jhk1SbUDwQW-zJW8BqneSd4YRpUjeuv1vOEVBikeQe3HFef5Gqrjm_UoN0H4HorrwHpEikff)

  

## Aim of the project

The aim of our project is to make it easier for people to meet each other in daily life. The members will share the activities they are going to do, and their friends will say whether they will join it or not.

## Roles of members

-   İbrahim Doğan (Design & Programming)
    
-   Burak Demirel (Tester)
    
-   Engin Can Höke (UI Design)
    
-   Recep Goger (Documentation)
    
-   Kadir Akgül (Analysis & Programming)
    

## Detailed timeline

1.  Analysis : 27-30 November
    
2.  Design  : 1-3 December
    
3.  Programming: 3-15 December
    
4.  UI Design: 4-15 December
    
5.  Testing : 7-16 December
    
6.  Documentation & Presentation : 10-16 December
    

![](https://lh6.googleusercontent.com/hgszLVwC26IqadU7WzE1bmKuZb2mbFDmfTAHS0Ks7aBOPxlvwgMhHxiVR-Pw-MfXOOq9coLx5GDPy8ezgNWm01AVn-JMc_M2r5Fez1799UPHac1Y7JMdJDbq4e400kVjV4U1krjE)

  

## Structure of system

The project is web application which is based on Python/Django Library. In Django, every application is called ‘Project’. Inside a project the modules called ‘app’. So we have ‘LetsMeet’ project and inside of it we have ‘main’ app which includes our web application. If we want to add ‘blog’ module in the future we are going to just create ‘blog’ app inside our ‘LetsMeet’ project.

  

Like every web application the django uses ‘Model View Controller’ structure. The Django project has urls.py which controlls every route value and redirects the request from route to controller. eg: example.com/events after / we see ‘events’ so our route is ‘event’ and it calls to views.events function which is act like controller. After the function call the request the view will be prepared for logged in user and shows the rendered page to the user.

## Structure of DB

Django has its own User Model. The Profile is extended version of User Model.

class Profile(models.Model):

user = models.OneToOneField(User, on_delete=models.CASCADE)

first_name = models.CharField(max_length=30, null=True)

last_name = models.CharField(max_length=30, null=True)

friends = models.ManyToManyField('self', blank=True)

image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

  

class FriendRequest(models.Model):

from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')

to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')

  

class EventOwner(models.Model):

profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)

  

class Event(models.Model):

time = models.DateTimeField()

createdTime = models.DateTimeField(null=True)

title = models.CharField(max_length=50)

owner = models.ForeignKey(EventOwner, on_delete=models.CASCADE, null=True)

location = models.CharField(max_length=150)

participants = models.ManyToManyField(Profile, blank=True)

description = models.TextField(blank=True, null=True)

url = models.CharField(max_length=500, blank=True, null=True)

  

![](https://lh3.googleusercontent.com/nChX01YtJS6SoZVgxImWdf9bvDWLaxOXuPJ8raF7L9z_UZRjsEH3dTPeU1_HnK42cw1I_uxva5nlwgS491RO7MQ1y5smIYEUb7eboq7LW99cdFyHpDY48fSYjQ5SAseCfdiS2ah-)

  

  

  
  

  
  

  

## Definitions of functions and subfunctions

This are only the functions heads and returns. To see what is inside the function check the appendix section.

  

-   This function returns 2 different output, if user not logged in it returns to signup/login page, if user logged in it returns to events feed.
    

def index(request):

return render(request, 'main/index.html', context)

return render(request, 'main/welcome.html')

  

-   This function returns specific events details
    

@login_required

def event(request, pk):

return render(request, 'main/event.html', context)

  

-   This function show the register form to register the user.
    

def register(request):

context = {'form': form}

return render(request, 'registration/register.html', context)

  

-   This function shows movies that top movies in theaters with their name , date and description. You can also can buy ticket by redirecting another website.
    

@login_required

def explore(request):

return render(request, 'main/explore.html', context)

  

-   The users can change the password username or email with this function. Also they are able to add image
    

@login_required

def updateProfile(request):

return redirect('profile', username=request.user.username)

  

-   This function returns the friends of user page.
    

@login_required

def friends(request):

return render(request, 'main/friends.html', context)

  

-   This function returns the logged in user’s profile page to see its profile or to change.
    

def profile(request, username):

return render(request, 'main/profile.html', context)

  

-   If another user add the user that is logged in as friend , you are able to add the user.
    

@login_required()

def addfriend(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

-   If user accepts the friend add request.
    

def acceptfriend(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

-   This function is for delete friend which is already your friend.
    

def deletefriend(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

-   If user rejects the friend add request
    

def rejectfriend(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

-   This function is for participate to event
    

def join(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

-   This function is for unparticipate to event
    

def unjoin(request, pk):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

-   This function is for create event.
    

def createEvent(request):

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

  

## Tests or critical cases

-   User's privacy: We encrypt people passwords and important informations inside database.
    
-   If user is not administrator it cannot reach admin panel.
    
-   Users only see events that are published by his/her friends.
    
-   If username already taken someone cannot take that username.
    
-   Password ;
    

-   can’t be too similar to your other personal information.
    
-   must contain at least 8 characters.
    
-   can’t be a commonly used password.
    
-   can’t be entirely numeric.
    

-   When register happens Django creates User, and we also create a Profile of User in database.
    
-   When event published it requires;
    

-   title
    
-   location
    
-   date
    
-   descriptions
    
-   Url (not necessarily)
    

-   You can’t add yourself as a friend.
    

## Future works

-   ## Commenting system can be added to the events. Users have to have a permit that allows them to comment positively or negatively.
    
-   ## Users can share their photos in past event on their profile and another users can like or dislike them. Like any kind of social media.
    
-   ## The “ Discovery” system also can be added. When any user create an event , there is a choice that allows the other user can see or not. Then in the discovery section all users can see available events.
    

  
  
  
  
  
  
  
  
  
  
  
  
  

## Software development tolls or platforms

[https://trello.com/b/uj4zRKT5/lets-meet](https://trello.com/b/uj4zRKT5/lets-meet)

[https://github.com/dedinededin/LetsMeet](https://github.com/dedinededin/LetsMeet)

  

![](https://lh3.googleusercontent.com/kMgxoqdg4H0o4dK8AOtxELFEiUAi0FHDgMU117BuQGzNo7DVOQpPL05PqRJKS331Z0vt_LgvJB4VpNb767kTgaEoKwdhJzFOjKqCg8lYYOTNrcOpU1I3E5fFXAQ5EMCqPpsvTBg4)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

## All code (as appendix)

from django.urls import path

from . import views

  

urlpatterns = [

path('', views.index, name='home'),

path('event/<int:pk>', views.event, name='events'),

path('event/join/<int:pk>', views.join),

path('event/unjoin/<int:pk>', views.unjoin),

path('register', views.register, name='register'),

path('explore', views.explore, name='explore'),

path('updateProfile', views.updateProfile, name='updateProfile'),

path('friends', views.friends, name='friends'),

path('<slug:username>', views.profile, name='profile'),

path('invite/accept/<int:pk>', views.acceptfriend),

path('invite/reject/<int:pk>', views.rejectfriend),

path('event/create', views.createEvent, name='createEvent'),

path('invite/<int:pk>', views.addfriend, name='addfriend'),

path('invite/del/<int:pk>', views.deletefriend, name='deletefriend')

]

  

from django.shortcuts import render, redirect

from .models import Profile, Event, EventOwner, FriendRequest

from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm, NewEventForm

from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from main.cinema_controller import get_films

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

import datetime

from django.utils.safestring import mark_safe

  
  

# Create your views here.

  

def index(request):

if request.user.is_authenticated:

profile = request.user.profile

friends = profile.friends.all()

owner_friends = EventOwner.objects.filter(profile__in=friends)

friends_events = Event.objects.filter(owner__in=owner_friends.all())

user_events = Event.objects.filter(owner=EventOwner.objects.get(profile=profile))

events = friends_events.union(user_events)

  

eventsUserParticipate = Event.objects.filter(participants=request.user.profile).order_by('-time').reverse()

  

context = {'home': 'active',

'events': events,

'eventsUserParticipate': eventsUserParticipate,

'friendRequests': request.user.profile.requests()}

  

return render(request, 'main/index.html', context)

else:

  

return render(request, 'main/welcome.html')

  
  

@login_required

def event(request, pk):

event = get_object_or_404(Event, pk=pk)

context = {'event': event}

  

return render(request, 'main/event.html', context)

  
  

def register(request):

if request.user.is_authenticated:

return redirect('home')

  

elif request.method == 'POST':

form = UserCreationForm(request.POST)

  

if form.is_valid():

form.save()

username = form.cleaned_data['username']

password = form.cleaned_data['password1']

email = form.cleaned_data['email']

first_name = request.POST.get('first_name')

last_name = request.POST.get('last_name')

  

user = User.objects.get(username=username)

profile = Profile(user=user, first_name=first_name, last_name=last_name)

profile.save()

eventowner = EventOwner(profile=profile)

eventowner.save()

user = authenticate(username=username, password=password)

login(request, user)

return redirect('home')

else:

form = UserCreationForm()

  

context = {'form': form}

return render(request, 'registration/register.html', context)

  
  

@login_required

def explore(request):

films = get_films()

films_up = films[:5]

films_down = films[5:]

context = {'explore': 'active', 'films': films, 'filmU': films_up, 'filmD': films_down,

'friendRequests': request.user.profile.requests()}

return render(request, 'main/explore.html', context)

  
  

@login_required

def updateProfile(request):

if request.method == 'POST':

u_form = UserUpdateForm(request.POST, instance=request.user)

p_form = ProfileUpdateForm(request.POST,

request.FILES,

instance=request.user.profile)

if u_form.is_valid() and p_form.is_valid():

u_form.save()

p_form.save()

return redirect('profile', username=request.user.username)

  
  

@login_required

def friends(request):

friends = request.user.profile.friends.all()

context = {'friends': 'active', 'Friends': friends,

'friendRequests': request.user.profile.requests()}

return render(request, 'main/friends.html', context)

  
  

def profile(request, username):

user = get_object_or_404(User, username=username)

profile = user.profile

friends = profile.friends.all()

owner = EventOwner.objects.filter(profile=user.profile)

  

context = {'home': 'active', 'User': user, 'friends': friends,

'name': profile.first_name + " " + profile.last_name}

  

if request.user.is_authenticated:

events = Event.objects.filter(owner__in=owner)

context['events'] = events

  

# wordList = list(filter(lambda a: a[index] == char, wordList))

isFriend = False

for friend in friends:

if friend == request.user.profile:

isFriend = True

break

print(isFriend)

  

if not isFriend:

button = '<a href="/invite/{}">' \

'<button type="button" class="btn btn-primary float-right">Add Friend</button>' \

'</a>'.format(profile.id)

context['frequestButton'] = mark_safe(button)

else:

button = '<a href="/invite/del/{}">' \

'<button type="button" class="btn btn-danger float-right">Delete Friend</button>' \

'</a>'.format(profile.id)

context['frequestButton'] = mark_safe(button)

  

if username == request.user.username:

context['frequestButton'] = ""

u_form = UserUpdateForm(instance=request.user)

p_form = ProfileUpdateForm(instance=request.user.profile)

context['u_form'] = u_form

context['p_form'] = p_form

context['friendRequests'] = request.user.profile.requests()

return render(request, 'main/profile.html', context)

  
  

@login_required()

def addfriend(request, pk):

profile = get_object_or_404(Profile, pk=pk)

frequest = FriendRequest(from_profile=request.user.profile, to_profile=profile)

frequest.save()

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def acceptfriend(request, pk):

to_accept = FriendRequest.objects.get(pk=pk)

to_accept.accept(request.user)

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def deletefriend(request, pk):

profile = get_object_or_404(Profile, pk=pk)

request.user.profile.friends.delete(profile)

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def rejectfriend(request, pk):

to_reject = FriendRequest.objects.get(pk=pk)

to_reject.reject()

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def join(request, pk):

event = get_object_or_404(Event, pk=pk)

event.participants.add(request.user.profile)

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def unjoin(request, pk):

event = get_object_or_404(Event, pk=pk)

event.participants.remove(request.user.profile)

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  
  

def createEvent(request):

if request.method == 'POST':

title = request.POST.get('title')

location = request.POST.get('location')

description = request.POST.get('description')

time = request.POST.get('datetimepicker1')

time = '2018-12-15 10:30'

owner = EventOwner.objects.get(profile=request.user.profile)

event = Event(title=title, location=location, description=description, owner=owner, time=time,

createdTime=datetime.datetime.now())

event.save()

print(title, location, description, time)

return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  

## Screen shots![](https://lh4.googleusercontent.com/IMJAzcmoPoWl_9SFCgrsjZZB8Qnw2DkNM7p-QpNvAEXHOR-yt0Jzwh1C_nzw9IxW1ifQTdr37V693_5QKTs33t7LLRb-R9VYS_oGxCnBoqnii2slNi7GAxwPCz6OwMbOudvBg4fK)![](https://lh5.googleusercontent.com/3-k3YV0kbTfAshK9q8Gb1pyg6wz4jvjbJMKvz7KxIf0ubYbUIsU0VtKegIPJU6RM-yV3zkaTU1pvmqC9K3t9jod2l1HnQSRwra5g7Easukn1UKcxXmd5ZvKYbMiuO84c9r45sLpQ)![](https://lh6.googleusercontent.com/NksUkmYMmz-T08L3Z6Yj9xUCt9t7S3oo9Zqsu13SxzfWNs0VgU5ZasVf99bTgM9ps5sNja0jHweDmZ8EbQfSpBufHhzduf8u8W1G6YFSlxGwBc24e0Yk8TaOFvSgPDRu5u7ktyfO)![](https://lh6.googleusercontent.com/Opj1dkRSKmLhEpW2cW6uxbZZnkvsR9jKv84d-sI9j4gfOW6Gmbbn0zCdeOgFNzAJFWQhgTJUS9x1HL9oieZWKCaCcDS92nQWH9ZjhaoH-h-iiFEwjnpXiyym3TptcHnH3gUbVcCl)![](https://lh3.googleusercontent.com/sgLUu75It3Qu4-LJPpQF7riqXfZ2O-KalTPFDngxN6R6JdE80jBWDyixZruZ7rCNdornnyduWhYMkfsJMN64Ve2Qnva1amXHAr5I0Oq5c8rcoUEpagB855uEMLRJE54XbzSqjQW4)![](https://lh6.googleusercontent.com/ApvP6CKTwrPz6jvsa4gSJQlg80cnPI81izzQBpDJmk12mCbwCXYF8-uK3AM6SEhliQ4Y3THgWvhjZYf4_t1YDAkZPTfkJWOwNh8QvKdy9lZyftmQn2xAjjSrW5sjZh2B1DwGieI7)![](https://lh6.googleusercontent.com/LPh4YJzQoiLYuOOdx5FW7UiynWdp6iPUDwpU0vcPvK9AnPYyw-6hA8hbYExaObxzwoqrEQVGUPXWwXsRVMFHbYDpZjOMVwC8p7pztodVFzkRXThISUFSXIGfrhc5awpSKTL7n3zZ)![](https://lh4.googleusercontent.com/vSI2_ilA1M3aD-7nUDt-amLlfY91Wvjfp40BM7a4yQ8GCFPUilcsv_trzG2Ed6aDpM7Jj5wQzJL1sinhzGB6D5BdWiQU5c-d6PSBncQdgXD9U29QSTdohVrcilBXO0I_bVI5fhpV)

## Resources

  

(n.d.). Retrieved from http://www.kennethcachia.com/plain-pattern/app/

Advanced Django Models - Python Django Tutorials. (n.d.). Retrieved from https://djangobook.com/advanced-models/

Best Free Pattern Generators for Designers - 27 to Choose From. (n.d.). Retrieved from https://www.whoishostingthis.com/resources/pattern-generators/

Bootstrap. (n.d.). Start Bootstrap. Retrieved from https://startbootstrap.com/

Bootstrap 3 Registration Form with Validation. (n.d.). Retrieved from https://codepen.io/juff03/pen/OXaXRG

Buildwithpython. (2018, September 07). Django 2.1 - Creating a Django App (StartApp) - 3/14. Retrieved from https://www.youtube.com/watch?v=ck8XDGnM2aA

D'Avignon, D. (2018, April 16). Django 2.0 - Make clicked tab active with Bootstrap. Retrieved from https://medium.com/@dustindavignon/django-2-0-make-clicked-tab-active-with-bootstrap-de27a74f6b76

Django template: Check for empty query set. (n.d.). Retrieved from https://stackoverflow.com/questions/17435233/django-template-check-for-empty-query-set

Django url pattern - string parameter. (n.d.). Retrieved from https://stackoverflow.com/questions/11894916/django-url-pattern-string-parameter

Django: How to Extend The User Model (aka Custom User Model). (2018, October 26). Retrieved from https://wsvincent.com/django-custom-user-model-tutorial/

Documentation. (n.d.). Retrieved from https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.exists

Goodridge, M. (2017, January 10). How to Upload and Display a Profile Picture in Django Development (Django Tutorial) | Part 36. Retrieved from https://www.youtube.com/watch?v=tT2JOpfelSg

HTML Snippets for Twitter Boostrap framework. (n.d.). Retrieved from https://bootsnipp.com/snippets/aMNV3

HTML Snippets for Twitter Boostrap framework. (n.d.). Retrieved from https://bootsnipp.com/snippets/56ExR

Printed, P. (2018, January 16). Django Authentication Basics. Retrieved from https://www.youtube.com/watch?v=dBctY3-Z5hY

Schafer, C. (2018, August 31). Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture. Retrieved from https://www.youtube.com/watch?v=FdVuKt_iuSI

The QuerySet value for an exact lookup must be limited to one result using slicing-Django. (n.d.). Retrieved from https://stackoverflow.com/questions/50431810/the-queryset-value-for-an-exact-lookup-must-be-limited-to-one-result-using-slici?noredirect=1&lq=1

Vitorfs. (2016, July 21). How to Extend Django User Model. Retrieved from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

Vitorfs. (2017, February 18). How to Create User Sign Up View. Retrieved from https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

Young, M. (n.d.). Image hover effects. Retrieved from https://miketricking.github.io/bootstrap-image-hover/
