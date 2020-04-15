from django.db import models
from django.forms import ModelForm
# Create your models here.

class student_table(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    student_branch = models.CharField(max_length = 50)

class teacher_table(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    salary = models.IntegerField(null=True)