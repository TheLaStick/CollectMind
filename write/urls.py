from django.urls import include, path
from . import views_main

urlpatterns = [

    path('', views_main.main, name='main'),

]
