from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Article

# Список всех статей
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

# Детальная информация о статье
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})

# Удаление статьи
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    article_title = article.title
    article.delete()
    return HttpResponse(f"Статья '{article_title}' успешно удалена!", content_type="text/plain")
