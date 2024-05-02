from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    path('get_answer', views.getAnswer, name='getAnswer')
]