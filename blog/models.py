from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
CHOICES = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='Published')


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
                               related_name='posts')
    title = models.CharField(max_length=150, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    slug = models.SlugField()
    status = models.CharField(max_length=50, choices=CHOICES, default='Draft')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

# title:  How to develop a django website --> Charfield
# date_time: DateTime
