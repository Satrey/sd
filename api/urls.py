from django.urls import path, include
from .views import TaskListView
from .views import TaskListAPIView, DetailTaskAPIView, ObjectListAPIView, DetailObjectAPIView, WorkerListAPIView, DetailWorkerAPIView, DispatcherListAPIView, DetailDispatcherAPIView


urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:pk>', DetailTaskAPIView.as_view()),
    path('objects/', ObjectListAPIView.as_view()),
    path('objects/<int:pk>', DetailObjectAPIView.as_view()),
    path('workers/', WorkerListAPIView.as_view()),
    path('workers/<int:pk>', DetailWorkerAPIView.as_view()),
    path('dispatchers/', DispatcherListAPIView.as_view()),
    path('dispatchers/<int:pk>', DetailDispatcherAPIView.as_view()),

]