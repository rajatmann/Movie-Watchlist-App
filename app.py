import datetime
import database

menu = """\nPlease select one of the following options:

1) Add new Movie.
2) View Upcoming movies.
3) View all movies.
4) watch a movie.
5) view watched movies.
6) Exit.

Your Selection: """

welcome = "\nWelcome to the watchlist app." 

print(welcome)

database.create_tables()

user_input = input(menu)

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date in (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f"--{heading} Movies--")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("---- \n")

def prompt_watch_movie():
    username = input("Enter full Username: ")
    movie_title = input("Enter the title of the movie: ")
    database.watch_movie(username, movie_title)

def print_watched_movies():
        username = input("Enter full Username: ")
        watched = database.get_watched_movie(username)
        print(f"\n---{username}'s Watched Movies--\n")
        for watch in watched:
            print(f"{watch[1]}")
        
        print("\n----")

while user_input != "6":

    if user_input == "1":
        prompt_add_movie()

    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)

    elif user_input == "3":
        movies = database.get_movies(False)
        print_movie_list("All", movies)

    elif user_input == "4":
        prompt_watch_movie()

    elif user_input == "5":
        print_watched_movies()

    else:
        print("Invalid input, please try again")
    user_input = input(menu) 
