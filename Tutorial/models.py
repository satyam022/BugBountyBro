from ckeditor.fields import RichTextField
from django.urls import reverse
from autoslug import AutoSlugField
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Create your models here.


class Course_category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('coursecategory', kwargs={'pk': self.pk})


class Tutorial_course(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    topic = models.CharField(max_length=50)
    image = models.ImageField(upload_to='tutorial/')
    video_id = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='topic', unique=True)
    category = models.ForeignKey(Course_category, on_delete=models.CASCADE)
    topic_title = models.TextField()
    Prerequisite = models.TextField()
    TopicCover = models.TextField()
    topic_details = RichTextField()
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic


class Problam(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    problam = models.CharField(max_length=255)
    describe_problem = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.username

