from django.shortcuts import render
from django.views import generic

from lab import models

from lab.form import UploadFileForm


class Mainpage(generic.TemplateView):
    template_name = 'lab/main_page.html'


class AllWorks(generic.ListView):
    template_name = 'lab/all_works.html'
    context_object_name = 'works'
    model = models.Work

    def get_queryset(self):
        qs = models.Work.objects.filter(grade=int(self.request.GET['grade']))
        return qs

    def get_context_data(self, **kwargs):
        return super(AllWorks, self).get_context_data(grade=self.request.GET['grade'])

class Work(generic.DetailView):
    context_object_name = 'work'
    model = models.Work

    def get_template_names(self):
        w = models.Work.objects.filter(id=int(self.request.GET['id'])).first()
        return [f'lab/{w.grade}/{w.url}']

    def get_context_data(self, **kwargs):
        form = UploadFileForm()
        return super(Work, self).get_context_data(form=form)

    def post(self, *args, **kwargs):
        work = models.Work.objects.get(id=kwargs['pk'])
        form = UploadFileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            author = self.request.POST['author']
            file = self.request.FILES['file']
            decision = models.Decision(work=work, author=author, file=file)
            decision.save()
        context = {'work': work, 'result': True, 'form': form}
        return render(request=self.request,
                      template_name=f'lab/{work.grade}/{work.url}',
                      context=context)