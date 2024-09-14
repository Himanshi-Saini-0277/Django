from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title
