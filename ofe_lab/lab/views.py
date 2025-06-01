from django.shortcuts import render
from django.views import generic

from lab import models


class Mainpage(generic.TemplateView):
    template_name = 'lab/main_page.html'


class AllWorks(generic.ListView):
    template_name = 'lab/all_works.html'
    context_object_name = 'works'
    model = models.Work

    def get_queryset(self):
        print(int(self.request.GET['grade']))
        qs = models.Work.objects.filter(grade=int(self.request.GET['grade']))
        print(qs)
        return qs

