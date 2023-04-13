from django.urls import path
from . import views


urlpatterns = [
    # 전체 게시글 조회, 게시글 생성
	path('articles/',views.article_list),
    
	# 상세 게시글 조회, 수정, 삭제
	path('articles/<int:article_pk>/', views.article_detail),
    
]
