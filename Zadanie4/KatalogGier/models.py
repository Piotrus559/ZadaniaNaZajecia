from django.db import models

class Gra(models.Model):
    Tytul = models.CharField(max_length=50)
    DataWydania = models.DateField()
    Tworcy = models.CharField(max_length=100)
    Wydawca = models.CharField(max_length=50)
    Dostepna = models.BooleanField()

    def __str__(self):
        return self.Tytul