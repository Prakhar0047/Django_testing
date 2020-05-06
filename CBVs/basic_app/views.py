from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School
    # Returns a list of school(Context_Dictionary). school_list --> this is made automatically by this. 
    # If you want to give context your own chosen name then use context_object_name = 'name_you_chose'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # In Detail View it just return lowerCaseModelName as Context_Dictionary school. You can edit in same way.

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School