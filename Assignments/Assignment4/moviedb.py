# COMP 1026 – Assignment 4

# Maaz Siddiqi

# Described the movie database, with functionality to add and find movies in the database.


from movie import Movie


class MovieDatabase:
    def __init__(self):
        """
        __init__
        Initializes Movie database with empty list
        """
        self.__database = list()

    def addMovie(self, title, year):
        """
        addMovie
        Adds a movie to the database
        :param title: title of the movie to add
        :param year: year of the movie to add
        :return: Nothing.
        """

        # Try to find movie in database, if it exists, throw error
        if self.findMovie(title, year) is not None:
            raise KeyError(f'Movie "{title}" already exists in database')
        else:
            # If it doesn't exist, make and add a new movie to database
            self.__database.append(Movie(title, year))

    def findMovie(self, title, year):
        """
        findMovie
        Finds a movie within the database
        :param title: Title of movie to find
        :param year: Year of movie to find
        :return: Movie within database, or None
        """

        # loop through database to find a movie with matching title and year
        for mov in self.__database:
            if title == mov.getTitle() and year == mov.getYear():
                # If found, return it
                return mov
        # If movie wasn't already found, it doesn't exist in database, return None
        return None

    def showAll(self):
        """
        showAll
        Shows an overview of all the movies in the database
        :return: Nothing.
        """
        movies = []

        # Fetch all movies as (title, year) pairs from database
        for mov in self.__database:
            movies.append((mov.getTitle(), mov.getYear()))

        # sort the list retrieved
        movies.sort()

        # output the movies as found through the sorted order in retrieved list
        for title, year in movies:
            # output brief overview of each movie
            print(self.findMovie(title, year).shortReview())
