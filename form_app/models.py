from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    file = models.FileField(upload_to='')

    def __str__(self):
        return self.name