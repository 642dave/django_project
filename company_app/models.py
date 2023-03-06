from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    age = models.IntegerField(max_length=50)
    department = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.name} {self.surname}"