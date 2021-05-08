from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from docker.models import Todo


# Create your views here.
def hello(request):
    return HttpResponse("Hello world")


class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'pub_date', 'finished']


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')


class TodoListView(ListView):
    model = Todo
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context