# Generated by Django 4.1.1 on 2022-10-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время закрытия'),
        ),
    ]
