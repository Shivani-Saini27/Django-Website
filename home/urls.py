"""
This is app file

"""

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name= 'home' ),
    path("about", views.about, name='about'),
    path("projects", views.projects, name='projects'),
    path("blog", views.blog, name='blog'),
    path("contacts", views.contacts, name='contacts'),
    path("todo", views.todo, name= 'todo')

]
