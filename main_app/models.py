from django.db import models

from django.urls import reverse
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})

class Child(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)

    #creat a event id FK
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} is {self.description}"