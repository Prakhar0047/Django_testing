from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_two(request):
    return HttpResponse('Hi im from testing two')