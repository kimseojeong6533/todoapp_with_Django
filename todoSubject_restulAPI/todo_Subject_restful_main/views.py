from django.shortcuts import render

# Create your views here.
from .models import TodoList
from .serializers import TodoSerializer
from django.views import View
from django.views import generic
from rest_framework import viewsets


class Todo_subject_restful_main(viewsets.ModelViewSet):   # serializer와 model을 연동
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
