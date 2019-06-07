# Generated by Django 2.1.5 on 2019-03-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('tid', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=150)),
                ('iscomplete', models.BooleanField(default=False)),
            ],
        ),
    ]