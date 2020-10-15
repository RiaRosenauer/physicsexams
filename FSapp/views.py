from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student, Professor

def home(request):
    return render(request, 'FSapp/home.html')

def set_of_exercises(request):

    context ={
        'exercises': Exercise.objects.all()
    }
    print(context['exercises'][0])
    return render(request, 'FSapp/set_of_exercises.html', context=context)

def favourites(request):
    return render(request, 'FSapp/favourites.html')

def to_repeat(request):
    return render(request, 'FSapp/to_repeat.html')

def exercise_view(request,pk):
    context={
        'exercise':Exercise.objects.filter(pk=pk)[0]
    }
    return render(request, 'FSapp/exercise_view.html',context)


# Create your views here.
