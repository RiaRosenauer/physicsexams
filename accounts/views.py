from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from FSapp.models import Student
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from django.urls import reverse

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        Student.objects.create(user=user)

        login(self.request, user)
        return HttpResponseRedirect('/exerciseSet/Aufgabensammlung')
