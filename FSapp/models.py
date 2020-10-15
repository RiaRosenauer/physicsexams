from django.db import models
from django.contrib.auth.models import User 
from django_mysql.models import ListCharField 
import datetime

# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)

    exam_type_choices = [
        ('p', 'Probeklausur'),
        ('k', 'Klausur'),
        ('w', 'Wiederholungsklausur')
    ]
    exam_type = models.CharField(
        max_length=10,
        choices=exam_type_choices,
        default='k'
    )

    year = models.IntegerField()


class Exercise(models.Model):

    name = models.CharField(max_length=100)

    question = models.TextField()
    answer = models.TextField()
    
    difficulty_choices = [
        ('e','einfach'),
        ('m','mittel'),
        ('s','schwer')
    ]
    difficulty = models.CharField(
        max_length=10,
        choices=difficulty_choices,
        default='e'
    )

    year = models.IntegerField()

    exam = models.ManyToManyField(Exam)

    course_choice = [
        ('EXP1', 'Experimentalphysik 1'),
        ('EXP2', 'Experimentalphysik 2'),
        ('EXP3', 'Experimentalphysik 3'),
        ('EXP4', 'Experimentalphysik 4'),
    ]

    course = models.CharField(
        max_length=10,
        choices=course_choice,
        default='EXP1'
    )

    subject = ListCharField(
        base_field = models.CharField(max_length=20),
        size = 5,
        max_length = 100
    )
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    solved_exercises = models.ManyToManyField(Exercise)

    failed_exercises = models.ManyToManyField(Exercise)

