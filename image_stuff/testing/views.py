from django.shortcuts import render
from django.http import HttpResponse
from testing.models import Topic, Webpage, AccesssRecord
# Create your views here.

def index(request):
    webpages_list = AccesssRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    my_dict = {'insert_me':'Im the template.'}
    return render(request,'testing/index.html', context=date_dict)