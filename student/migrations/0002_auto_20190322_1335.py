# Generated by Django 2.1.5 on 2019-03-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(),
        ),
    ]
