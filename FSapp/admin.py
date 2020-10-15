from django.contrib import admin
from FSapp.models import Exam, Exercise, Student
# Register your models here.

admin.site.register(Exam)
admin.site.register(Student)
admin.site.register(Exercise)