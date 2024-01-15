
import os

from django.db import models


# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(null=True, blank=True, upload_to='Files')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension


