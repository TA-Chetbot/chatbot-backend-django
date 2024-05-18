from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    path('get_answer', views.getAnswer, name='getAnswer'),
    path('preprocess_question', views.preprocess, name='preprocess_question')
]