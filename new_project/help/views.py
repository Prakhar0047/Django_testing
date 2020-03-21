from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(request):
    help_dict = {'help':'Help Page'}
    return render(request, 'help/help.html', context=help_dict)