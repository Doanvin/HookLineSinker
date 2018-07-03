from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    site = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField()
    date_exp = models.DateField()
    type = models.CharField(max_length=30, null=True, blank=True)
    rating = models.IntegerField()
    report = models.TextField(max_length=500, null=True, blank=True)
    access = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.date)