from django.urls import path
from .views import article_list, article_detail, article_delete

urlpatterns = [
    path('articles/', article_list, name='article-list'),         # GET /articles/
    path('articles/<int:id>/', article_detail, name='article-detail'),  # GET /articles/:id
    path('articles/<int:id>/delete/', article_delete, name='article-delete'),  # DELETE /articles/:id/delete/
]
