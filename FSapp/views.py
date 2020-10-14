from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe

def home(request):
    return render(request, 'FSapp/home.html')

# Create your views here.
