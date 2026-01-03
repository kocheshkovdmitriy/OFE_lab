from django.contrib.auth import logout, login, authenticate
from django.http import FileResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic


from datetime import datetime

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
            grade_id=models.Grade.objects.get(name=int(self.request.GET['grade']))).order_by('number')
        return qs

    def get_context_data(self, **kwargs):
        return super(AllWorks, self).get_context_data(grade=self.request.GET['grade'])

class Work(generic.DetailView):
    template_name = 'lab/detail_work.html'
    context_object_name = 'work'
    model = models.Work


    def get_context_data(self, **kwargs):
        return super(Work, self).get_context_data(
            classes=models.Grade.objects.all(),
            letters=models.Letter.objects.all(),
            grade=None,
            letter=None,
            flag=False
        )

    def post(self, *args, **kwargs):
        print(self.request.POST)
        print(self.request.FILES)
        work = models.Work.objects.get(id=kwargs['pk'])
        grade = self.request.POST.get('grade', None)
        let = self.request.POST.get('letter', None)
        context = {'work': work,
                   'letters': models.Letter.objects.all(),
                   'classes': models.Grade.objects.all(),
                   'students': models.Student.objects.filter(grade_id=grade, label_id=let),
                   'result': False, 'flag': True, 'grade': grade, 'letter': let, }
        if self.request.POST.get('button2'):
            if self.request.FILES.get('file') and self.request.POST.get('student'):
                print("форма валидна")
                author = models.Student.objects.get(id=self.request.POST.get('student'))
                file = self.request.FILES['file']
                format = file.name[file.name.rfind('.'):]
                file.name = f'{author.get_name()}_{work.get_number()}_{datetime.now().strftime("%d-%m-%Y_%H%M%S")}{format}'
                print('Имя сохраняемого файла:', file.name)
                protocol = models.Protocol(work=work, author=author, file=file)
                protocol.save()
                context['result']=True


        return render(request=self.request,
                      template_name='lab/detail_work.html',
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


class Protocols_work(generic.View):
    def get(self, request, **kwargs):
        context=self.get_context_data(**kwargs)
        return render(request=request, template_name='lab/protocols_work.html', context=context)

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request=request, template_name='lab/protocols_work.html', context=context)

    def get_queryset(self, **kwargs):
        print(self.request.POST)
        if self.request.POST.get('button1'):
            return models.Protocol.objects.filter(work_id=int(kwargs.get('pk')),
                                                  accepted=True,
                                                  author__in=models.Student.objects.filter(
                                                      grade_id=int(self.request.POST.get('grade')),
                                                      label_id=int(self.request.POST.get('letter')))
                                                  )
        if self.request.POST.get('button2') and self.request.POST.get('student'):
            return models.Protocol.objects.filter(work_id=int(kwargs.get('pk')), author_id=int(self.request.POST.get('student')), accepted=True)
        return models.Protocol.objects.filter(work_id=int(kwargs.get('pk')), accepted=True)

    def get_context_data(self, **kwargs):
        context = {
            'protocols': self.get_queryset(**kwargs),
            'work': models.Work.objects.get(id=int(kwargs.get('pk'))),
            'classes': models.Grade.objects.all(),
            'letters': models.Letter.objects.all(),
            'grade': self.request.POST.get('grade'),
            'letter': self.request.POST.get('letter'),
            'student': self.request.POST.get('student'),
            'flag': self.request.POST.get('button1', False) or self.request.POST.get('button2', False),
            }
        if self.request.POST.get('grade') and self.request.POST.get('letter'):
            context['students'] = models.Student.objects.filter(
                                                      grade_id=int(self.request.POST.get('grade')),
                                                      label_id=int(self.request.POST.get('letter')))
        return context


def download_file_view(request, pk):
    object = models.Protocol.objects.get(id=pk)
    return FileResponse(object.file.open(), as_attachment=True, filename=object.file.name)


def logout_view(request):
    logout(request)
    return redirect('/')


class Accept_protokols(generic.View):
    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request=request,
                      template_name='lab/accept_protocols.html',
                      context=context)

    def get_queryset(self, **kwargs):
        return models.Protocol.objects.filter(accepted=False)

    def get_context_data(self, **kwargs):
        return {
            'protocols': self.get_queryset(**kwargs)
        }


def edit_protocol(request, pk):
    protocol = models.Protocol.objects.get(id=int(pk))
    protocol.accepted = True
    protocol.save()
    return redirect('/protocols_accept/')

def delete_protocol(request, pk):
    protocol = models.Protocol.objects.get(id=int(pk))
    protocol.delete()
    return redirect('/protocols_accept/')
