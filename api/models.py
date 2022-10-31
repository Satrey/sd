from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=12, blank=True, null=False, verbose_name='Номер телефона мобильный')
    phone_number_worked = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефона рабочий')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.last_name


class Object(models.Model):
    number = models.IntegerField(blank=False, null=False, verbose_name='Номер объекта')
    address = models.CharField(max_length=100, blank=False, null=False, verbose_name='Адрес объекта')
    latitude = models.FloatField(max_length=15, null=True, blank=True, verbose_name='Широта')
    longitude = models.FloatField(max_length=15, null=True, blank=True, verbose_name='Долгота')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Описание для СМИ')
    status = models.BooleanField(blank=False, verbose_name='Статус')

    class Meta:
        ordering = ["number"]
        verbose_name = 'Объект'
        verbose_name_plural = "Объекты"

    def __str__(self):
        return self.address


class Dispatcher(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Отчество')
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=12, blank=True, null=False, verbose_name='Номер телефона мобильный')
    phone_number_worked = models.CharField(max_length=12, blank=True, null=True, verbose_name='Номер телефона рабочий')

    class Meta:
        verbose_name = 'Диспетчер'
        verbose_name_plural = "Диспетчеры"

    def __str__(self):
        return self.last_name


class Task(models.Model):
    number = models.IntegerField(null=False, blank=False, verbose_name='Номер заявки')
    task_start = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Время открытия')
    address = models.ForeignKey(Object, null=False, blank=False, on_delete=models.PROTECT, verbose_name='Адрес объекта')
    bug_description = models.TextField(max_length=255, null=False, blank=False, verbose_name='Описание неисправности')
    sender = models.CharField(max_length=50, blank=False, null=False, verbose_name='Кто передал')
    dispatcher = models.ForeignKey(Dispatcher, null=False, on_delete=models.PROTECT, verbose_name='Принял диспетчер')
    worker = models.ForeignKey(Worker, null=False, on_delete=models.PROTECT, verbose_name='Назначен исполнитель')
    job_description = models.TextField(max_length=255, blank=True, null=True, verbose_name='Описание выполненных работ')
    job_doc_number = models.IntegerField(blank=True, null=True, verbose_name='Номер акта выполненных работ')
    task_end = models.DateTimeField(blank=True, null=True, verbose_name='Время закрытия')
    task_status = models.BooleanField(blank=True, null=True, default=False, verbose_name='Статус заявки')

    class Meta:
        ordering = ["number"]
        verbose_name = 'Заявка'
        verbose_name_plural = "Заявки"

    def __str__(self):
        return self.bug_description



