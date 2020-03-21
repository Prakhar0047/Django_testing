from django.shortcuts import render
from django.http import HttpResponse
from user.models import details
# Create your views here.

def user(request):

    names = details.objects.order_by('first_name')
    name_dict = {'Names':names}
    return render(request,'user/user.html', context=names)