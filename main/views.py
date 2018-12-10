from django.shortcuts import render, redirect
from .models import Profile, Event, EventOwner
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from main.cinema_controller import get_films


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        friends = profile.friends.all()
        owner = EventOwner.objects.filter(profile=request.user.profile)
        events = Event.objects.filter(owner__in=owner)
        context = {'home': 'active', 'friends': friends, 'events': events,
                   'name': profile.first_name + " " + profile.last_name}
        return render(request, 'main/index.html', context)
    else:
        context = {'home': 'active'}
        return render(request, 'main/index.html', context)


def events(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        friends = profile.friends.all()
        owner_friends = EventOwner.objects.filter(profile__in=friends)
        events = Event.objects.filter(owner__in=owner_friends.all())

        context = {'events': 'active', 'events': events}
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
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def explore(request):
    films = get_films()
    films_up = films[:5]
    films_down = films[5:]
    context = {'explore': 'active', 'films': films, 'filmU': films_up, 'filmD': films_down}
    return render(request, 'main/explore.html', context)
