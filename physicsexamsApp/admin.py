from django.contrib import admin
from physicsexamsApp.models import Exam, Exercise, Student,Professor, Subject, Course
# Register your models here.

admin.site.register(Exam)
admin.site.register(Student)
admin.site.register(Exercise)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Course)
