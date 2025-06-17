from django.contrib.auth import logout, login, authenticate
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.files.storage import FileSystemStorage

from lab import models

from lab import forms


class Mainpage(generic.TemplateView):
    template_name = 'lab/main_page.html'


class AllWorks(generic.ListView):
    template_name = 'lab/all_works.html'
    context_object_name = 'works'
    model = models.Work

    def get_queryset(self):
        qs = models.Work.objects.filter(
            grade_id=models.Grade.objects.get(name=int(self.request.GET['grade'])))
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
        if self.request.GET.get('choice', None):
            form_class = forms.ChoiceClass(self.request.GET)
            form_protocol = forms.UploadFileForm(
                grade=self.request.GET.get('grade', None),
                lit=self.request.GET.get('litter', None))
            return super(Work, self).get_context_data(
                form_class=form_class,
                form_protocol=form_protocol,
                flag=True
            )
        else:
            form_class = forms.ChoiceClass()
            return super(Work, self).get_context_data(
                form_class=form_class,
                flag=False
            )

    def post(self, *args, **kwargs):
        print(self.request.POST)
        work = models.Work.objects.get(id=kwargs['pk'])
        form_protocol = forms.UploadFileForm(self.request.POST, self.request.FILES)
        if form_protocol.is_valid():
            '''author = self.request.POST['author']
            file = self.request.FILES['file']
            decision = models.Decision(work=work, author=author, file=file)
            decision.save()'''
        context = {'work': work, 'result': True, 'form': form_protocol}
        return render(request=self.request,
                      template_name=f'lab/{work.grade}/{work.url}',
                      context=context)

class LoginView(generic.View):
    def get(self, request):
        form = forms.AuthUser()
        context = {'form': form}
        return render(request, 'lab/auth_user.html', context=context)

    def post(self, request):
        form = forms.AuthUser(request.POST)
        if form.is_valid():
            username = 'teacher'
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    form.add_error('__all__', 'Учетная запись не активна.')
            else:
                form.add_error('__all__', 'Неверно введены имя пользователя или пароль.')
        context = {'form': form}
        return render(request, 'lab/auth_user.html', context=context)

class Protocols_work(generic.ListView):
    template_name = 'lab/decisions_work.html'
    context_object_name = 'decisions'
    model = models.Protocol

    def get_queryset(self):
        qs = models.Protocol.objects.filter(work_id=int(self.request.GET['id']))
        return qs

def download_file_view(request, pk):
    object = models.Protocol.objects.get(id=pk)
    return FileResponse(object.file.open(), as_attachment=True, filename=object.file.name)


def logout_view(request):
    logout(request)
    return redirect('/')