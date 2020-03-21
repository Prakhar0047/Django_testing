from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_two, name = 'test_two'),
]