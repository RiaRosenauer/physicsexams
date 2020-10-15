from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/exerciseSet', views.set_of_exercises, name='set_of_exercises'),
    path('/favourites', views.favourites, name='favourites'),
    path('/toRepeat', views.to_repeat, name='to_repeat')
]