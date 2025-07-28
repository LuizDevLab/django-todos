from .models import Todo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.
class TodoListView(ListView):
  model = Todo

class TodoCreateView(CreateView):
  model = Todo
  fields = ["title", "deadline"]
  success_url =  reverse_lazy("todo_list")