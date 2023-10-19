from django.shortcuts import render
from django.contrib.staticfiles.finders import find
from .models import Film
# Create your views here.
def load_films(request):
    file_ = find('dicts/6-letter-words.txt')
    with open(file_) as f:
        data =f.read()
    
    newFilms = 0
    lenOfData = len(data)
    for item in range(0, len(data)):
        film_row = data[item].rstrip('\n')
        poster,title,released,cert,duration,genre,iMDB_Rating,overview,director,star1,star2,star3,star4,gross = film_row.split(',')
        if not Film.objects.filter(title=title).exists():
            obj = Film.objects.update_or_create(
                title = title,
                released=released,
                certficate=cert,
                duration=duration,
                genre=genre,
                director=director,
                star1=star1,
                star2=star2,
                star3=star3,
                star4=star4,
                overview=overview,
                poster=poster
            )
            newFilms += 1
        print(f"Adding Films {round((item/lenOfData)*100,2)}%")