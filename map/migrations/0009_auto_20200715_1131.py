# Generated by Django 3.0.8 on 2020-07-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20200715_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huntingspot',
            name='address',
        ),
        migrations.RemoveField(
            model_name='huntingspot',
            name='geom1',
        ),
    ]
