from Player import Player


class Batter(Player):
    def __init__(self, id, teams, hits, HRs, batting_avg):
        super().__init__(id, teams)
        self.__hits = hits
        self.__HRs = HRs
        self.__batting_avg = batting_avg

    def __repr__(self):
        return super().__repr__() + ' {} hits, {} HRs, Average: {}'.format(self.__hits, self.__HRs, self.__batting_avg)

    def __lt__(self, other):
        return self.__batting_avg <= other.__batting_avg