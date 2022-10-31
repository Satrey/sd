from django.contrib import admin
from .models import Worker, Object, Dispatcher, Task

admin.site.register(Worker)
admin.site.register(Dispatcher)
admin.site.register(Task)
admin.site.register(Object)
