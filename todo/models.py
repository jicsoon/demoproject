from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    tid = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=150)
    iscomplete = models.BooleanField(default=False)

    
    def __str__(self):
        return "{}. {}".format(self.tid,self.content)

    def get_absolute_url(self):
        return reverse("complete", kwargs={"todo_id": self.tid})