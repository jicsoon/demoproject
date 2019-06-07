from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return '{}. {}'.format(self.id,self.name)

