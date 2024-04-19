from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ToDoList

class Todolist(LoginRequiredMixin,ListView):
    #model = ToDoList

    template_name = 'main/todo.html'

    def get_queryset(self):
        task = ToDoList.objects.filter(author = self.request.user)
        return task

    
        
    
class Add(LoginRequiredMixin,CreateView):
    model = ToDoList
    fields = ['content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Edit(LoginRequiredMixin,UpdateView):
    model = ToDoList
    fields = ['content']
    success_url = '/'


class Delete(LoginRequiredMixin,DeleteView):
    model = ToDoList
    success_url = '/'