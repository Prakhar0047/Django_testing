from django.contrib import admin
from .models import student_table, teacher_table
# Register your models here.
admin.site.register(student_table)
admin.site.register(teacher_table)
