# Generated by Django 4.1.1 on 2022-10-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_object_address_alter_object_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['number'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
    ]
