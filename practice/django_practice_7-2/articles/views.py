from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer,ArticleListSerializer
from django.shortcuts import get_object_or_404

# 전체 조회
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    else: # POST
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) -> raise_exception=True의 역할

#상세 조회
@api_view(['GET','PUT','DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    else: # DELETE
        article.delete()
        data = {
            'delete':f'데이터 {article_pk}번이 삭제되었습니다.'
		}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
