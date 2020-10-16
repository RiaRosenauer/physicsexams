from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student, Professor, Subject, Course 
from django.http import JsonResponse 
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'FSapp/home.html')

def set_of_exercises(request): 
    search = request.GET.get('search') if request.GET.get('search') != None else ''
    
    #To DO 
    data = request.GET

    course = data.get('filter_course') if data.get('filter_course') != None else ''
    exam_type = data.get('filter_exam_type') if data.get('filter_exam_type') != None else '' 
    year = data.get('filter_year') if data.get('filter_year') != None else '' 
    subjects = data.get('filter_subjects') if data.get('filter_subjects') != None else '' 

    print(course, exam_type, year, subjects)
    context ={
        'exercises': Exercise.objects.filter(name__icontains=search)
    }

    if request.is_ajax():
        html = render_to_string('FSapp/exercise_query.html', context=context)
        return JsonResponse(html, safe=False) 

    mode = 'Aufgabensammlung' if request.get_full_path()=='/exerciseSet/Aufgabensammlung' else 'Klausur'
    context = {
        'mode':mode,
        'exercises': Exercise.objects.all(),
        'subjects': Subject.objects.all(),
        'courses': Course.objects.all(),

    }

    return render(request, 'FSapp/set_of_exercises.html', context=context)

@login_required
def favourites(request):
    student = Student.objects.filter(user=request.user)[0]
    context = {
        'exercises': student.favourite_exercises.all(),
        'subjects': Subject.objects.all(),
        'courses': Course.objects.all(),
    }
    print(student.favourite_exercises.all(), context['courses'],Course.objects.all())

    return render(request, 'FSapp/favourites.html', context=context)

@login_required
def to_repeat(request):
    student = Student.objects.filter(user=request.user)[0]
    print(student.failed_exercises.all())
    context = {
        'exercises': student.failed_exercises.all(),
        'subjects': Subject.objects.all(),
        'courses': Course.objects.all(),
    }
    return render(request, 'FSapp/to_repeat.html', context)

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
    'favourite_exercise': favourite,
    'professor': exercise.exam.all()[0].professor
    }

    return render(request, 'FSapp/exercise_view.html',context)


# Create your views here.
