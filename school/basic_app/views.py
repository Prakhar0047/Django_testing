from django.shortcuts import render
from basic_app import forms
# Create your views here.

def index(request):
    return render(request, 'Base/index.html')

def student(request):
    form = forms.the_form()

    if request.method == 'POST':
        form = forms.the_form(request.POST)

        if form.is_valid():
            print('Success')
            form.save(commit=True)
            return index(request)
    return render(request, 'stuff/student.html', {'form':form})

def teacher(request):
    form = forms.teacher_form()

    if request.method == 'POST':
        form = forms.the_form(request.POST)

        if form.is_valid():
            print('Success')
            form.save(commit=True)
            return index(request)
    return render(request, 'stuff/teacher.html', {'form':form})

def form_name_view(request):
    form = forms.the_form()

    if request.method == 'POST':
        form = forms.the_form(request.POST)

        if form.is_valid():
            print('Success')
            form.save(commit=True)
            return index(request)

    return render(request,'stuff/form_page.html',{'form':form})