# Generated by Django 4.1.1 on 2022-10-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_task_job_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['number'], 'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
