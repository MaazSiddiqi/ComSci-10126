class Player:
    def __init__(self, id, team):
        self.__id = id
        self.__team = team

    def __repr__(self):
        return '{} ({})'.format(self.__id, self.__team)
