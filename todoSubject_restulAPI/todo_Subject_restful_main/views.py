from django.shortcuts import render

# Create your views here.
from .models import TodoList
from .serializers import TodoSerializer, TodoDetailSerializer, TodoCreateSerializer
from django.views import View
from django.views import generic
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView, CreateAPIView


# class Todo_subject_restful_main(viewsets.ModelViewSet):   # serializer와 model을 연동
#     queryset = TodoList.objects.all()
#     serializer_class = TodoSerializer

class Todo_subject_restful_main(ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_detail(RetrieveAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoDetailSerializer

class Todo_subject_restful_update(UpdateAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_delete(DestroyAPIView):
    lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer

class Todo_subject_restful_create(CreateAPIView):
    # lookup_field = 'no'
    queryset = TodoList.objects.all()
    serializer_class = TodoCreateSerializer



