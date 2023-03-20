from django.contrib import admin
#python manage.py shell_plus 해서 데이터베이스에 제목 컨텐트 작성해서 넣어도됨
from .models import Article 
# Register your models here.

admin.site.register(Article)
