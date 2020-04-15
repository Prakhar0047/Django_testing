from django import forms

from basic_app.models import student_table, teacher_table

class the_form(forms.ModelForm):
    class Meta:
        model = student_table
        fields =  '__all__'

class teacher_form(forms.ModelForm):
    class Meta:
        model = teacher_table
        fields =  '__all__'