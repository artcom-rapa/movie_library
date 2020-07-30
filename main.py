
import random
from datetime import date


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.views = 0

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1
        return print(self)


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} - {self.season}{self.episode}"


class Library:
    def __init__(self):
        self.movie_database = [
            Movie(title="Turu. W pogoni za sławą", year="2019", genre="Animation"),
            Movie(title="Pulp Fiction", year="1994", genre="Thriller"),
            Movie(title="The Godfather", year="1972", genre="Thriller"),
            Movie(title="Sugar Man", year="2012", genre="Documentary"),
            Movie(title="Shrek", year="2001", genre="Animation"),
            Movie(title="Schindler's List", year="1993", genre="History"),
            Movie(title="Lion King", year="1994", genre="Animation"),
            Movie(title="Ice Age", year="2002", genre="Animation"),
            Movie(title="The Old Guard", year="2020", genre="Fantasy"),
            Movie(title="Madagascar", year="2005", genre="Animation"),
            Movie(title="Joker", year="2019", genre="Thriller"),
            Series(title="Game of Thrones", year="2011", genre="Fantasy", season="S01", episode="E01"),
            Series(title="Game of Thrones", year="2011", genre="Fantasy", season="S01", episode="E02"),
            Series(title="Game of Thrones", year="2011", genre="Fantasy", season="S01", episode="E03"),
            Series(title="Game of Thrones", year="2011", genre="Fantasy", season="S02", episode="E01"),
            Series(title="Friends", year="1994", genre="Comedy", season="S01", episode="E01"),
            Series(title="Friends", year="1994", genre="Comedy", season="S01", episode="E02"),
            Series(title="Friends", year="1994", genre="Comedy", season="S02", episode="E01"),
            Series(title="The Witcher", year="2019", genre="Fantasy", season="S01", episode="E01")
        ]

    def get_movies(self):
        self.movies_only = [item for item in self.movie_database if (isinstance(item, Movie) and not isinstance(item, Series))]
        return sorted(self.movies_only, key=lambda movie: movie.title )

    def get_series(self):
        self.series_only = [item for item in self.movie_database if isinstance(item, Series)]
        return sorted(self.series_only, key=lambda series: series.title)

    def search(self, keyword):
        for item in self.movie_database:
            if item.title == keyword:
                return item
            else:
                pass
        else:
            return "Brak filmu w bibliotece!"

    def generate_views(self):
        self.movie_database[random.randint(0, len(self.movie_database)-1)].views += random.randint(100, 1000)
        return True

    def top_titles(self, content_type=None, top_counter=3):
        if content_type == None:
            return sorted(self.movie_database, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Movie":
            self.movies_only = [item for item in self.movie_database if (isinstance(item, Movie) and not isinstance(item, Series))]
            return sorted(self.movies_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        elif content_type == "Series":
            self.series_only = [item for item in self.movie_database if isinstance(item, Series)]
            return sorted(self.series_only, key=lambda movie: movie.views, reverse=True)[0:top_counter]
        else:
            return 0


if __name__ == "__main__":
    print("\nHello! Welcome to the movie library!\n")
    library = Library()

    print("Function get_movies():\n")
    for movie in library.get_movies():
        print(movie.title)
    print("")

    print("Function get_series():\n")
    for series in library.get_series():
        print(f"{series.title} {series.season}{series.episode}")
    print("")

    print("Function search(Schindler's List) - (TRUE):\n")
    print(library.search("Schindler's List"))
    print("")

    print("Function search(Avatar) - (FALSE):\n")
    print(library.search("Avatar"))
    print("")

    print("Function generate_views():\n")
    for i in range(10):
        library.generate_views()
    print("")

    print("Function top_titles():\n")
    print(f"The most popular movies and series of the day {date.today()}:\n")
    for item in library.top_titles(content_type="Movie", top_counter=7):
        print(f"{item.title}: {item.views}")
    print("")
