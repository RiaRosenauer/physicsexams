from django.db import models
from django.contrib.auth.models import User 
from django_mysql.models import ListCharField 


# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name 

class Exam(models.Model):
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor,null=True, blank=True, on_delete=models.CASCADE)

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

    year = models.CharField(
        max_length=10,
        default='20'
    )

    
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    course_choice = [
        ('EXP1', 'Experimentalphysik 1'),
        ('EXP2', 'Experimentalphysik 2'),
        ('EXP3', 'Experimentalphysik 3'),
        ('EXP4', 'Experimentalphysik 4'),
    ]

    course = models.CharField(
        max_length=10,
        choices=course_choice,
        default='e'
    )

    name = models.CharField(max_length=100)


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

    exam = models.ManyToManyField(Exam, blank=True)

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

    subject = models.ManyToManyField(Subject, blank=True)
    

    image1 = models.ImageField(upload_to='LatexImages/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    solved_exercises = models.ManyToManyField(Exercise, null=True, blank=True,related_name='student_solved')

    failed_exercises = models.ManyToManyField(Exercise,null=True, blank=True, related_name='student_failed')

