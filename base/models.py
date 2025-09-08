from django.db import models
'''
(models.Model) tells Django 
“this class is a model, 
map it to a database table, and give it ORM superpowers.”

from django.some_module import SomeClassOrFunction
models → module/package (django.db.models).
Model → class inside that module.
'''

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    # user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:50]