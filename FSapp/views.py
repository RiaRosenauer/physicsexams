from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from FSapp.models import Exam, Exercise, Student, Professor, Subject, Course 
from django.http import JsonResponse 
from django.template.loader import render_to_string
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

    context = {
        'exercises': Exercise.objects.all(),
        'subjects': Subject.objects.all(),
        'courses': Course.objects.all(),

    }

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
