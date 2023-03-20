from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # db에 자동으로 현재 시간을 업데이트하겠다 단골 시험문제야!!
    updated_at = models.DateTimeField(auto_now=True)
    # 새롭게 등록될때 자동으로 시간을 등록해주겠다.(생성시간 등록)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.title}'