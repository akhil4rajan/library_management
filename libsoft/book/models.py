from django.db import models

class Book(models.Model):
    """
    Model config of Algo
    """
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    year_of_publication = models.CharField(max_length=250)
    availability = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name