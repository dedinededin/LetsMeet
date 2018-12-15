from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('events', views.events, name='events'),
    path('register', views.register, name='register'),
    path('explore', views.explore, name='explore'),
    path('updateProfile', views.updateProfile, name='updateProfile'),
    path('friends', views.friends, name='friends'),
    path('<slug:username>', views.profile, name='profile')
]
