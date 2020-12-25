from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import generic
from .models import Todo_list


class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        # template_name = 'todo_board/todo_board_list.html'
        template_name = 'todo_board/todo_board_list.html'
        todo_list = Todo_list.objects.all()
        return render(request, template_name, {"todo_list": todo_list})
