from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pages(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts', null=True)
    text = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ded_moroz: page_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])