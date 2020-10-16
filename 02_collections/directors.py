'''
Get the 20 highest rated directors based on their average movie IMDB ratings.
Parse movie_metadata.csv: use csv.DictReader which gives a bunch of OrderedDicts.
Use these key, value pairs: director_name, movie_title, title_year, imdb_score.
Consider only the directors with a minimum of 4 movies.
Consider only movies of year >= 1960.
Print the top 20 highest rated directors with their movies ordered descending on rating.

Michael Stucki
16 October 2020
'''

import csv
from collections import defaultdict

MIN_YEAR = 1960
MIN_FILMS = 4
FILM_CSV = 'movie_metadata.csv'
RANKING_LIMIT = 20


def compute_average_score(movies):
    average = 0.0
    total = 0.0
    count = 0
    for movie in movies:
        score = movie['imdb_score']
        if score:
            try:
                total += float(score)
                count += 1
            except ValueError:
                pass

    average = total / count
    return average


if __name__ == '__main__':

    movies_collection = defaultdict(list)
    directors = set()
    with open (FILM_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            year = row['title_year']
            if year and int(year) >= MIN_YEAR:
                d = {'movie_title': row['movie_title'],
                     'title_year': row['title_year'],
                     'imdb_score': row['imdb_score']}
                movies_collection[row['director_name']].append(d)
                directors.add(row['director_name'])

    director_averages = dict()
    for director in directors:
        movies = movies_collection[director]
        if len(movies) >= MIN_FILMS:
            average = compute_average_score(movies)
            director_averages[director] = average

    sorted_director_averages = sorted(director_averages.items(), key=lambda x: x[1], reverse=True)

    for i in range(RANKING_LIMIT):
        director = sorted_director_averages[i][0]
        print(f'{(i+1):02}. {director:75} {sorted_director_averages[i][1]:.1f}')
        print('-' * 83)

        for movie in sorted(movies_collection[director], key = lambda x: x['title_year'], reverse=True):
            print(f'{movie["title_year"]}] {movie["movie_title"]:73} {movie["imdb_score"]}')

        print()

