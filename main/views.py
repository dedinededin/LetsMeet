from django.shortcuts import render, redirect
from .models import Profile, Event, EventOwner
from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm, NewEventForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from main.cinema_controller import get_films
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        events = Event.objects.all()

        eventsUserParticipate = Event.objects.filter(participants=request.user.profile)

        context = {'home': 'active', 'events': events, 'eventsUserParticipate': eventsUserParticipate}

        return render(request, 'main/index.html', context)
    else:

        return render(request, 'main/welcome.html')


@login_required
def events(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        friends = profile.friends.all()
        owner_friends = EventOwner.objects.filter(profile__in=friends)
        events = Event.objects.filter(owner__in=owner_friends.all())

        context = {'events': 'active', 'Events': events}
        return render(request, 'main/events.html', context)

    else:
        context = {'events': 'active'}
        return render(request, 'main/events.html', context)


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
    context = {'explore': 'active', 'films': films, 'filmU': films_up, 'filmD': films_down}
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
    context = {'friends': 'active', 'Friends': friends}
    return render(request, 'main/friends.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    friends = profile.friends.all()
    owner = EventOwner.objects.filter(profile=user.profile)
    events = Event.objects.filter(owner__in=owner)
    context = {'home': 'active', 'User': user, 'friends': friends, 'events': events,
               'name': profile.first_name + " " + profile.last_name}

    if username == request.user.username:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context['u_form'] = u_form
        context['p_form'] = p_form

    return render(request, 'main/profile.html', context)


