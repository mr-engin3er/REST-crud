from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name
