class Frac:
    def __init__(self, num, denom):
        if denom == 0:
            raise ZeroDivisionError

        self.__num = num
        self.__denom = denom

    def __repr__(self):
        return f'{self.__num}/{self.__denom}'

    def __mul__(self, other):
        return Frac(self.__num * other.__num, self.__denom * other.__denom)

    def __add__(self, other):
        return Frac((self.__num * other.__denom) + (other.__num * self.__denom), self.__denom * other.__denom)

    def __float__(self):
        return self.__num/self.__denom

    def __eq__(self, other):
        if self.__num * other.__denom == other.__num * self.__denom:
            return True
        else:
            return False

