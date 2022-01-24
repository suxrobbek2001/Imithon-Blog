from django.contrib.auth.models import User
from django.db import models


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    sana = models.DateField()
    mavzu = models.CharField(max_length=300)
    matn = models.TextField()
    muallif = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mavzu}, {self.muallif}"

