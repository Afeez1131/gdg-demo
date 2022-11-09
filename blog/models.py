from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CHOICES = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
                               related_name='posts')
    title = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    slug = models.SlugField()
    status = models.CharField(max_length=50, choices=CHOICES, default='Draft')

    def __str__(self):
        return self.title

# title:  How to develop a django website --> Charfield
# date_time: DateTime
