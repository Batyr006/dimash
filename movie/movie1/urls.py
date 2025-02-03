from django.urls import path
from .views import movie_list, movie_detail, movie_delete

urlpatterns = [
    path('movies/', movie_list, name='movie-list'),           # GET /movies/
    path('movies/<int:id>/', movie_detail, name='movie-detail'),  # GET /movies/:id
    path('movies/<int:id>/delete/', movie_delete, name='movie-delete'),  # DELETE /movies/:id/delete/
]
