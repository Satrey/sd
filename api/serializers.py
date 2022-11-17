from rest_framework import serializers
from .models import Task, Object, Worker, Dispatcher



class TaskSerializer(serializers.ModelSerializer):
    address = serializers.SlugRelatedField(read_only=True, slug_field='address')
    dispatcher = serializers.SlugRelatedField(read_only=True, slug_field='last_name')
    worker = serializers.SlugRelatedField(read_only=True, slug_field='last_name')

    class Meta:
        model = Task
        fields = (
            'id',
            'number',
            'task_start',
            'address',
            'bug_description',
            'sender',
            'dispatcher',
            'worker',
            'job_description',
            'job_doc_number',
            'task_end',
            'task_start',
            'task_status'
        )


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = (
            'id',
            'number',
            'address',
            'latitude',
            'longitude',
            'description',
            'status',
        )


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'phone_number_worked',
        )


class DispatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatcher
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
        )
        

