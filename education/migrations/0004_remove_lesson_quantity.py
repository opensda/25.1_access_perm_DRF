# Generated by Django 4.2.6 on 2023-10-29 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_lesson_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='quantity',
        ),
    ]