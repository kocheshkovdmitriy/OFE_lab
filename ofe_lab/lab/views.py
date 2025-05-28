from django.shortcuts import render
from django.views import generic


class Mainpage(generic.TemplateView):
    template_name = 'lab/main_page.html'


class Lab5Class(generic.TemplateView):
    template_name = 'lab/5_class_all.html'

class Lab6Class(generic.TemplateView):
    template_name = 'lab/6_class_all.html'

class Lab7Class(generic.TemplateView):
    template_name = 'lab/7_class_all.html'

class Lab8Class(generic.TemplateView):
    template_name = 'lab/8_class_all.html'

class Lab9Class(generic.TemplateView):
    template_name = 'lab/9_class_all.html'

class Lab10Class(generic.TemplateView):
    template_name = 'lab/10_class_all.html'

class Lab11Class(generic.TemplateView):
    template_name = 'lab/11_class_all.html'