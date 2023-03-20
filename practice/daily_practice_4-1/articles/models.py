from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title}'