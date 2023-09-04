from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/home'