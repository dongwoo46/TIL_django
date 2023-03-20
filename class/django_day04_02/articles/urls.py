from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    #개별적 게시글을 볼수잇는 detail 함수 <int:pk>가 valueable routing
    path('detail/<int:pk>/', views.detail, name='detail'),
    
    # 새 글 생성하는 url
    # path('new/', views.new, name='new'),

    #작성한글 db저장하는 url
    path('create/', views.create, name='create'),

    # 글 삭제하기
    path('delete/<int:pk>', views.delete, name='delete'),

    #글 수정하기
    # path('edit/<int:pk>',views.edit, name='edit'),
    path('update/<int:pk>/',views.update, name='update'),
]

