from django.conf.urls import patterns, url


urlpatterns = patterns(
    'core.views',

    url(r'^$', 'todo_list_view', name='core-todo-list'),
    url(r'^create/$', 'todo_create_view', name='core-todo-create'),
    url(r'^delete/(?P<pk>[\d]+)/$', 'todo_delete_view', name='core-todo-delete'),
    url(r'^toggle/(?P<pk>[\d]+)/$', 'todo_toggle_view', name='core-todo-toggle'),
)
