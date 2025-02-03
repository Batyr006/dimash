from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Movie

# Список всех фильмов
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Детальная информация о фильме
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Удаление фильма
def movie_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie_title = movie.title
    movie.delete()
    return HttpResponse(f"Фильм '{movie_title}' успешно удалён!", content_type="text/plain")
