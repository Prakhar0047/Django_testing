from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('student/', views.student, name='student'),
    path('teacher/', views.teacher, name='teacher'),
    path('form_page/', views.form_name_view, name='form')
]