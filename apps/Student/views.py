from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from Student.models import Student
from Student.forms import StudentForm
# Create your views here.


def index(request):
    words = 'Word'
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    return render(request, 'index.html', locals())


class IndexView(View):
    template_name = 'index.html'
    
    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context
    
    def get(self, request):
        context = self.get_context()
        form = StudentForm()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)
    
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({
            'form': form
        })
        return render(request, self.template_name, context=context)

