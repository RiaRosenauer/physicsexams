from django.db import models
from django.contrib.auth.models import User 
from django_mysql.models import ListCharField 
from smart_selects.db_fields import ChainedManyToManyField


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

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Subject(models.Model):
    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Exercise(models.Model):

    name = models.CharField(max_length=100)

    question = models.TextField()
    answer = models.TextField()

    preview = models.TextField(null=True, blank=True)
    
    difficulty_choices = [
        (u'&#x2B51; &#x2606; &#x2606;','einfach'),
        (u'&#x2B51; &#x2B51; &#x2606;','mittel'),
        (u'&#x2B51; &#x2B51; &#x2B51;','schwer')
    ]

    difficulty = models.CharField(
        max_length=40,
        choices=difficulty_choices,
        default='e'
    )

    year = models.IntegerField(blank=True, null=True)

    exam = models.ManyToManyField(Exam, blank=True)

    exerciseNumber = models.IntegerField(blank=True, null=True)

    course = models.ForeignKey(Course,null=True, blank=True, on_delete=models.CASCADE)

    subject = ChainedManyToManyField(
        Subject,
        horizontal=True,
        chained_field="course",
        chained_model_field="course",
        verbose_name='subject')

    image1 = models.ImageField(upload_to='LatexImages/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    solved_exercises = models.ManyToManyField(Exercise, null=True, blank=True,related_name='student_solved')

    failed_exercises = models.ManyToManyField(Exercise,null=True, blank=True, related_name='student_failed')

    favourite_exercises = models.ManyToManyField(Exercise,null=True, blank=True, related_name='student_favourite')

    def __str__(self):
        return self.user.username