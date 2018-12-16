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
