# COMP 1026 – Assignment 4

# Maaz Siddiqi

# Describes the Movie object, with functionality to add reviews


class Movie:
    def __init__(self, title, year):
        """
        __init__
        Initializes Movie Object
        :param title: title of movie object
        :param year: year of movie object
        """

        # Assign parameters to object private variables
        self.__title = title
        self.__year = year

        # Initialize reviews array, 6 indexes,
        # [0] for average of reviews,
        # [i] tacks number of reviews corresponding to the index value.
        self.__reviews = [0] * 6


    def addReview(self, review):
        """
        addReview
        Adds a review to the movie object
        :param review: value of review
        :return: Nothing.
        """

        # If review isn't within valid range, ignore review addition
        if review < 1 or review > 5:
            return

        # Increment review count of index in reviews array corresponding to review value
        self.__reviews[review] += 1

    def shortReview(self):
        """
        shortReview
        Provide a brief description of the Movie object, includes title, year, and average review
        :return: Output string containing summary
        """
        # Output string
        # Rounds average calculation in format string
        return '{} ({}): {:0.1f}/5'.format(self.__title, self.__year, self.__calcAverage())

    def longReview(self):
        """
        Provides a detailed description of Movie object, includes title, year, average review, and specific review counts
        :return: Output string containing summary
        """

        # Output string
        out = f'{self.__title} ({self.__year})\n' + \
              f'Average review: {self.__calcAverage():0.1f}/5\n' + \
              f'*****: {self.__reviews[5]}\n' + \
              f'**** : {self.__reviews[4]}\n' + \
              f'***  : {self.__reviews[3]}\n' + \
              f'**   : {self.__reviews[2]}\n' + \
              f'*    : {self.__reviews[1]}'

        return out

    def getTitle(self):
        """
        getTitle
        Fetches title of Movie Object
        :return: Title of movie object
        """
        return self.__title

    def getYear(self):
        """
        getYear
        Fetches year of Movie Object
        :return: Year of movie object
        """
        return self.__year

    def __calcAverage(self) -> float:
        """
        calcAverage
        Calculates the average of all the reviews stored in movie object
        :return: The average review of Movie
        """

        reviews_sum = 0
        reviews_count = 0

        # For each review in reviews array, get index (review value) and value (review count)
        for review, count in enumerate(self.__reviews):
            # Skip index 0 since it stores average review
            if review == 0:
                continue

            # Add to total review value sum
            reviews_sum += review * count
            # increment total number of reviews by count
            reviews_count += count

        # if at the end of review array examination, no reviews were analyzed, return 0 average
        if reviews_count == 0:
            return 0.0

        # otherwise, return the average of the reviews
        avg = reviews_sum / reviews_count
        return avg
