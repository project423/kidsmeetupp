from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about,name='about'),
    path('events/', views.events_index, name='events'),
    path('profile/', views.profile, name='profile'),
    path('events/<int:event_id>', views.events_detail, name ='detail'),   
     
]