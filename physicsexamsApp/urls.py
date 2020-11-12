from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 

urlpatterns = [
    path('', views.set_of_exercises, name='home'),
    path('admin', admin.site.urls),
    path('exerciseSet/Aufgabensammlung', views.set_of_exercises, name='set_of_exercises_a'),
    path('exerciseSet/Klausur', views.set_of_exercises, name='set_of_exercises_k'),
    path('exerciseSet/Klausur/<int:pk>', views.exam_view, name='exam_view'),
    path('favourites', views.favourites, name='favourites'),
    path('toRepeat', views.to_repeat, name='to_repeat'),
    path('toRepeat_ajax', views.to_repeat_ajax, name='to_repeat_ajax'),
    path('exerciseSet/<int:pk>',views.exercise_view, name='exercise_view'), 
    path('exerciseSet/currentExercise_ajax',views.exercise_view_ajax, name='exercise_view_ajax'), 
    path('exerciseSet/favourite_ajax', views.favourite_ajax, name='favourite_ajax')
]

 
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

