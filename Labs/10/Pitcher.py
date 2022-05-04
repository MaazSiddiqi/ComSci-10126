from Player import Player


class Pitcher(Player):
    def __init__(self, id, team, wins, losses, era):
        super().__init__(id, team)
        self.__wins = wins
        self.__losses = losses
        self.__era = era

    def __repr__(self):
        return super().__repr__() + ' {} W, {} L, ERA: {}'.format(self.__wins, self.__losses, self.__era)

    def __lt__(self, other):
        return self.__era <= other.__era
