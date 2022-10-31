from django.test import TestCase
from .models import Task, Object, Worker, Dispatcher


class TaskModelTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        Task.objects.create(number='1', bug_description='Test Description',)


