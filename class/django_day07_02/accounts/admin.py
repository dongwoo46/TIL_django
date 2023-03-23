from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User # 새롭게 정의한 유저

# Admin page에서 user관리 pasge의 인터페이스 설정
admin.site.register(User, UserAdmin)