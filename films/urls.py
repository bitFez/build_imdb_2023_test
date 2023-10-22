from django.urls import path

from .views import homepage, film_detail, load_films

app_name = "films"

urlpatterns = [
    path("", homepage, name="home"),
    path("film/<int:pk>", film_detail, name="film_d"),
    path("load_films", load_films, name="load_f"),
]
