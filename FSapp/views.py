from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student, Professor
from django.http import JsonResponse 
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'FSapp/home.html')

def set_of_exercises(request): 
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    print(search)
    
    context ={
        'exercises': Exercise.objects.filter(name__icontains=search)
    }
    if request.is_ajax():
        html = render_to_string('FSapp/exercise_query.html', context=context)

        return JsonResponse(html, safe=False) 

    return render(request, 'FSapp/set_of_exercises.html', context=context)

def favourites(request):
    return render(request, 'FSapp/favourites.html')

def to_repeat(request):
    return render(request, 'FSapp/to_repeat.html')

@login_required
def exercise_view_ajax(request):
    solved = request.GET.get('solved')
    exercise = request.GET.get('exercise')

    student = Student.objects.filter(user=request.user)[0]

    if solved == 'true':
        student.solved_exercises.add(exercise)
        student.failed_exercises.remove(exercise)
    else:
        student.solved_exercises.remove(exercise)
        student.failed_exercises.add(exercise)
    return JsonResponse({})


@login_required
def favourite_ajax(request):
    exercise = request.GET.get('exercise')
    favourite = request.GET.get('favourite')
    student = Student.objects.filter(user=request.user)[0]
    if favourite == 'true':
        student.favourite_exercises.add(exercise)
    else:
        student.favourite_exercises.remove(exercise)
    return JsonResponse({})






@login_required
def exercise_view(request,pk):
    exercise = Exercise.objects.filter(pk=pk)[0]

    student = Student.objects.filter(user=request.user)[0]
    if exercise in student.solved_exercises.all():
        solved = True
        already_done = True
    else:
        if exercise in student.failed_exercises.all():
            already_done = True
            solved = False
        else:
            solved = False
            already_done = False
    if exercise in student.favourite_exercises.all():
        print(student.favourite_exercises.all())
        favourite = True
    else:
        favourite = False

    context={
    'exercise': exercise,
    'solved': solved,
    'already_done': already_done,
    'favourite_exercise': favourite
    }


    return render(request, 'FSapp/exercise_view.html',context)


# Create your views here.
