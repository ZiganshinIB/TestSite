from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy


def index(request):
    return HttpResponse('Hello world')


class Curses(ListView):
    model = Curse
    # template_name = ""
    # context_object_name = ""
    # extra_context = {"": ... ,}  for static fild

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[" "] = ""
    #     return context

    def get_queryset(self):
        return Curse.objects.filter(is_published=True)


class CursesByGroup(ListView):
    model = Curse

    def get_queryset(self):
        return Curse.objects.filter(group_id=self.kwargs["group_id"])


class Homeworks(ListView):
    model = Homework


class HomeworksByCurse(ListView):
    model = Homework

    def get_queryset(self):
        print(self.kwargs)
        return Homework.objects.filter(curse_id=self.kwargs['curse_id'])


def get_curse(request, pk):
    model = Curse.objects.get(pk=pk)
    template_name = 'univer/curse.html'
    context = {
        'object': model
    }
    return render(request,template_name, context)


def create_homework(request, curse_id):
    curse = Curse.objects.get(pk=curse_id)
    if request.method == "POST":
        form = HomeworkForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            Homework.objects.create(**form.cleaned_data)
            return redirect('homeworks', curse.pk)
    else:
        form = HomeworkForm(initial={'curse': curse})
    context = {
        'form': form,
        'curse': curse,
    }
    return render(request, 'univer/homework_form.html', context)


class CreateGroup(CreateView):
     form_class = GroupForm
     template_name = "univer/groupc_form.html"
     url = "curses"


class CreateCurse(CreateView):
    form_class = CurseForm
    template_name = "univer/curse_form.html"

# def get_homework(request):
#     homeworks = Homework
#
#     return  render(request)

