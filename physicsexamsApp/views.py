from django.shortcuts import render
from django.utils.safestring import mark_safe
from physicsexamsApp.models import Exam, Exercise, Professor, Subject, Course 
from django.http import JsonResponse 
from django.template.loader import render_to_string



def home(request):
    return render(request, 'physicsexamsApp/home.html')


def set_of_exercises(request): 
    search = request.GET.get('search') if request.GET.get('search') != None else ''


    #To DO 
    data = request.GET

    course = data.get('filter_course') if data.get('filter_course') != None else ''
    exam_type = data.get('filter_exam_type') if data.get('filter_exam_type') != None else '' 
    year = data.get('filter_year') if data.get('filter_year') != None else '' 
    subjects = data.get('filter_subjects') if data.get('filter_subjects') != None else '' 

    exams_data = [exam for exam in Exam.objects.all()]

    #fiter search and year.
    exercises = Exercise.objects.filter(name__icontains=search,  year__icontains=year)
    #filter course 

    context ={
        'exercises': Exercise.objects.filter(name__icontains=search),
    }

    if request.is_ajax():
        html = render_to_string('physicsexamsApp/exercise_query.html', context=context)
        return JsonResponse(html, safe=False) 

    mode = 'Aufgabensammlung' if request.get_full_path()=='/exerciseSet/Aufgabensammlung' else 'Klausur'

    context = {
        'mode':mode,
        'exams': exams_data,
        'exercises': Exercise.objects.all(),
        'subjects': Subject.objects.all(),
        'courses': Course.objects.all(),
    }
    return render(request, 'physicsexamsApp/set_of_exercises.html', context=context)



def exercise_view(request,pk):
    exercise = Exercise.objects.filter(pk=pk)[0]

    context={
    'exercise': exercise,
    'exams': exercise.exam.all(),
    'MEDIA_URL':'/media/'
    }

    return render(request, 'physicsexamsApp/exercise_view.html',context)

def exam_view(request, pk):
    exam = Exam.objects.filter(pk=pk)[0]

    context={
        'exam':exam,
        'exercises':exam.exercise_set.all(),
        'MEDIA_URL':'/media/'
    }
    print()
    return render(request, 'physicsexamsApp/exam_view.html', context)

# Create your views here.
