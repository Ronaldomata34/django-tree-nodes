from django import forms
from django.urls import path
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from . import views
from .models import Node

app_name = 'nodes'
urlpatterns = [
    #path('', views.show_nodes),
    path('detail/<int:pk>/', DetailView.as_view(model=Node, context_object_name='node'), name="node_detail"),
    path('update/<int:pk>/', views.UpdateNode.as_view(model=Node, fields=['name', 'parent']), name="node_update"),
    path('delete/<int:pk>/', views.DeleteNode.as_view(model=Node), name="node_delete"),
    path('create/', CreateView.as_view(model=Node, fields=['name', 'parent']), name="node_create"),
    path('list/', ListView.as_view(model=Node, context_object_name='nodes'), name="node_list"),
]

