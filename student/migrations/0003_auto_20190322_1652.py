# Generated by Django 2.1.5 on 2019-03-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190322_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grad_date',
            field=models.DateField(),
        ),
    ]