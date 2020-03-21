from django.urls import path
from first_testing import views

urlpatterns = [
    path('', views.index, name = 'index'),
]