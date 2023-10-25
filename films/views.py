from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.staticfiles.finders import find
import re
from datetime import datetime, date, timedelta
from django.utils.dateparse import parse_duration
from .models import Film


import os
module_dir = os.path.dirname(__file__)  # get current directory

# Create your views here.
def homepage(request):
    films_list = Film.objects.all()

    context = {"films":films_list}
    return render(request, "films/homepage.html", context)

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)

    context = {"film":film}
    return render(request, "films/film_detail.html", context)


def load_films(request):
    file_ = find('films_data.txt')
    file_path = os.path.join(module_dir, 'films_data3.txt')
    with open(file_path, "r", encoding='utf-8') as f:
        data =f.readlines()
    
    newFilms = 0
    lenOfData = len(data)
    for item in range(0, len(data)):
        film_row = data[item].rstrip('\n')
        poster,title,released,cert,duration,genre,iMDB_Rating,overview,director,star1,star2,star3,star4,gross = re.split(r',(?=")',film_row)
        released = f'{released[1:-1]}-01-01'
        dur=f'{duration[1:-5]}'
        f_dur = timedelta(minutes=int(dur))
        if not Film.objects.filter(title=title).exists():
            obj = Film.objects.update_or_create(
                title = title,
                released=released,
                certificate=cert,
                duration=f_dur,
                genre=genre,
                director=director,
                star1=star1,
                star2=star2,
                star3=star3,
                star4=star4,
                overview=overview,
                poster=poster,
                gross=int(gross[1:-1].replace(',', ''))
            )
            newFilms += 1
        print(f"Adding Films {round((item/lenOfData)*100,2)}%")
    return redirect("/")