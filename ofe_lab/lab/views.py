from django.shortcuts import render
from django.views import generic


class Mainpage(generic.TemplateView):
    template_name = 'lab/main_page.html'
