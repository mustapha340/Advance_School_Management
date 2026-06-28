from django.urls import path
from . import views

urlpatterns = [
    # Link itakayofungua list ya wanafunzi (mfano: http://127.0.0.1:8000/)
    path('', views.student_list, name='student_list'),
]