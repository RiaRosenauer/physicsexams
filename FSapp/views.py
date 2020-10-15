from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student, Professor
from django.http import JsonResponse 
def home(request):
    return render(request, 'FSapp/home.html')

def set_of_exercises(request): 
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    print(search)
    
    context ={
        'exercises': Exercise.objects.filter(name__icontains=search)
    }
    if request.is_ajax():
        exercise_query(request)

        #return JsonResponse(list(Exercise.objects.filter(name__icontains=search)), safe=False) 
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

def exercise_query(request):
    print('sdfsdf')

    return render(request, 'FSapp/exercise_query.html',context={})
# Create your views here.
