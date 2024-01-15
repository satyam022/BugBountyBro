from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class News(models.Model):
    ntitle = models.CharField(max_length=100)

    def __str__(self):
        return self.ntitle


class Category(models.Model):
    category = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='category', unique=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('moviescategory', kwargs={'slug': self.slug})


class Movie(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    video = models.FileField(upload_to="videos/%y")
    slug = AutoSlugField(populate_from='title', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Language = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Comments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comm = models.TextField()


class SubComments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comm = models.TextField()
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE)

