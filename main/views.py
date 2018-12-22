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

        today = datetime.datetime.today()

        friends_events = Event.objects.filter(owner__in=owner_friends.all()).filter(time__gte=today)
        user_events = Event.objects.filter(owner=EventOwner.objects.get(profile=profile)).filter(time__gte=today)
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

        isFriend = False
        for friend in friends:
            if friend == request.user.profile:
                isFriend = True
                break

        if not isFriend:
            button = '<a href="/invite/{}">' \
                     '<button type="button" class="btn btn-primary float-right">Add Friend</button>' \
                     '</a>'.format(profile.id)
            context['events'] = None
            context['frequestButton'] = mark_safe(button)
        else:
            button = '<a href="/invite/del/{}">' \
                     '<button type="button" class="btn btn-danger float-right">Delete Friend</button>' \
                     '</a>'.format(profile.id)
            context['frequestButton'] = mark_safe(button)

        frequests = FriendRequest.objects.filter(from_profile=request.user.profile, to_profile=profile)
        if frequests.count() > 0:
            button = '<a href="">' \
                     '<button type="button" class="btn btn-primary float-right" disabled>Request Sent</button>' \
                     '</a>'.format(profile.id)
            context['events'] = None
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
    request.user.profile.friends.remove(profile)
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
        time = request.POST.get('datetimepicker')
        url = request.POST.get('url')
        owner = EventOwner.objects.get(profile=request.user.profile)
        event = Event(title=title, location=location, description=description, owner=owner, time=time,
                      createdTime=datetime.datetime.now(), url=url)
        event.save()
        print(title, location, description, time)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deleteEvent(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.owner.profile == request.user.profile:
        event.delete()
    return redirect('home')


def search(request):
    if request.method == 'POST':
        keyword = str(request.POST.get('keyword'))
        words = keyword.split(" ")

        results = None
        if (len(keyword) > 2):
            for word in words:
                username = Profile.objects.filter(user__username__contains=word)
                profile = Profile.objects.filter(first_name__contains=word) | Profile.objects.filter(
                    last_name__contains=word)
                results = username.union(profile)
        context = {'results': results}
        return render(request, 'main/search.html', context)
