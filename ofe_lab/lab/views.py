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
        form_class = forms.ChoiceClass()
        return super(Work, self).get_context_data(
            form_class=form_class,
            flag=False
        )

    def post(self, *args, **kwargs):
        print(self.request.POST)
        work = models.Work.objects.get(id=kwargs['pk'])
        form_class = forms.ChoiceClass(self.request.POST)
        form_protocol = forms.UploadFileForm(
            grade=self.request.POST.get('grade', None),
            lit=self.request.POST.get('litter', None))
        context = {'work': work, 'result': False, 'flag': True, 'form_class': form_class,
                   'form_protocol': form_protocol}

        if  self.request.POST.get('button2'):
            if self.request.FILES.get('file') and self.request.POST.get('students'):
                print("форма валидна")
                author = models.Student.objects.get(id=self.request.POST.get('students'))
                file = self.request.FILES['file']
                protocol = models.Protocol(work=work, author=author, file=file)
                protocol.save()
                context['result']=True


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
    template_name = 'lab/protocols_work.html'
    context_object_name = 'protocols'
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