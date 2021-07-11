from django.urls import path
from django.urls.resolvers import URLPattern

from main import views


urlpatterns=[
    path('projects/',views.projects,name='projects'),
    path('languages/',views.languages,name='languages'),
    path('',views.index,name='index')
]