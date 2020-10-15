from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student

def home(request):
    return render(request, 'FSapp/home.html')

def set_of_exercises(request):

    context ={
        'exercises':Exercise.objects.all()
    }
    print(context['exercises'][0])
    return render(request, 'FSapp/set_of_exercises.html')

def favourites(request):
    return render(request, 'FSapp/favourites.html')

def to_repeat(request):
    return render(request, 'FSapp/to_repeat.html')





# Create your views here.
