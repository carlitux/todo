from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from .models import Todo


class TodoListView(ListView):
    model = Todo
    paginate_by = 10
    context_object_name = 'todos'  # default is object_list


class TodoCreateView(CreateView):
    model = Todo
    success_url = reverse_lazy('core-todo-list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('core-todo-list')


class TodoToggleView(SingleObjectMixin, View):
    model = Todo

    def post(self, *args, **kwargs):
        object = self.get_object()
        object.done = not object.done
        object.save()

        return HttpResponseRedirect(reverse_lazy('core-todo-list'))

todo_list_view = TodoListView.as_view()
todo_create_view = TodoCreateView.as_view()
todo_delete_view = TodoDeleteView.as_view()
todo_toggle_view = TodoToggleView.as_view()
