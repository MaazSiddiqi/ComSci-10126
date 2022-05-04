# COMP 1026 – Assignment 4

# Maaz Siddiqi

# A sophisticated movie reviewing system that manages a database for movies. This is the main file which handles the
# processing of saved data.

from moviedb import MovieDatabase

COMMAND = 0
TITLE = 1
YEAR = 2
REVIEW = 3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'

movieDB = MovieDatabase()


def new_mov(title, year):
    """
    new_mov
    Adds a new movie to the database
    :param title: title of movie to add
    :param year: year of movie to add
    :return: Nothing.
    """

    # tries to add the movie to database,
    try:
        movieDB.addMovie(title, year)
    except KeyError:
        # if movie already exists, an error is thrown
        return


def mov_rev(title, year, review):
    """
    mov_rev
    Adds a review to a movie in the database, if it exist
    :param title: title used to identify movie
    :param year: year used to identify movie
    :param review: review to add to movie, if movie is found in database
    :return: Nothing.
    """

    # finds the movie in the database
    mov = movieDB.findMovie(title, year)

    # exit function if movie isn't found
    if mov is None:
        return

    # if found, add a review to it
    mov.addReview(review)


def show_db():
    """
    show_db
    Provides quick overview of database by showing all short reviews for all movies in the database
    :return: Nothing.
    """

    movieDB.showAll()


def print_mov(title, year):
    """
    print_mov
    Provides a detailed overview of a specific movie in the database, if it exists.
    :param title: title used to identify movie
    :param year: year used to identify movie
    :return: Nothing.
    """

    # first find movie,
    mov = movieDB.findMovie(title, year)

    # if found, show its review
    if mov is not None:
        print(mov.longReview())


def readFile(inp):
    """
    readFile
    Extracts and executes the database commands stored in data file
    :param inp: Name of data file containing database commands
    :return:
    """

    # Tries to open and read data file containing database commands
    try:
        with open(inp, 'r') as fh:

            # Interpret individual command found on each line
            for line in fh:
                data = line.strip().split('-')

                command = data[COMMAND]

                # Based on command type, execute its respective function
                if command == NEW_COMMAND:
                    title = data[TITLE]
                    year = data[YEAR]

                    # YOUR CODE FOR PROCESSING NEW COMMANDS
                    new_mov(title, year)

                elif command == REVIEW_COMMAND:
                    title = data[TITLE]
                    year = data[YEAR]
                    review = int(data[REVIEW])

                    # YOUR CODE FOR PROCESSING REV COMMANDS
                    mov_rev(title, year, review)

                elif command == SHOW_COMMAND:
                    show_db()

                elif command == PRINT_COMMAND:
                    title = data[TITLE]
                    year = data[YEAR]
                    print_mov(title, year)
    except FileNotFoundError:
        # if the file isn't found, throw an error
        raise FileNotFoundError


def main():

    # Loop input prompt until valid input file is given.
    while True:
        # Prompt user for file name input
        mov_file = input('Enter the name of the file: ')

        # Try read file, if file could not be found, prompt again.
        try:
            readFile(mov_file)
            break
        except FileNotFoundError:
            print(f'File "{mov_file}" not found, please try again.')


main()
