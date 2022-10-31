from django.views.generic import ListView
from rest_framework import generics
from .serializers import TaskSerializer, ObjectSerializer, DispatcherSerializer, WorkerSerializer
from .models import Task, Object, Dispatcher, Worker


class TaskListView(ListView):
    model = Task
    template_name = 'api_doc.html'


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTaskAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ObjectListAPIView(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class DetailObjectAPIView(generics.RetrieveAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer


class WorkerListAPIView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class DetailWorkerAPIView(generics.RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class DispatcherListAPIView(generics.ListAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer


class DetailDispatcherAPIView(generics.RetrieveAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer
