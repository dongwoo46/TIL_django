from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('ssafy/',views.greeting, name='greeting'),
    path('index/',views.index, name='index'),
    path('lotto/',views.lotto, name="lotto")
]
