YEAR = 0
LEAGUE = 1
TEAM = 2
GAMES_PLAYED = 3
GAMES_WON = 4
GAMES_LOST = 5
WON_WS = 6
RUNS = 7
AT_BAT = 8
HITS = 9
DOUBLES = 10
TRIPLES = 11
HOME_RUNS = 12
ATTENDANCE = 13

NON_INT_COLS = [LEAGUE, TEAM, WON_WS]


def get_data():
    all_data = []
    with open('Teams.csv', 'r') as fh:
        headers = fh.readline()
        for line in fh:
            data = line.strip().split(',')
            for i in range(len(data)):
                if i not in NON_INT_COLS:
                    data[i] = int(data[i])
                elif i == WON_WS:
                    data[i] = (data[i] == 'Y')

            all_data.append(data)

    return all_data


teams = get_data()

most_home_runs = teams[0]
total_attendance_in_1999 = 0
lowest_win_rate_but_won = teams[0]
highest_win_rate_but_lost = teams[0]

for team in teams:

    most_home_runs = team if team[HOME_RUNS] > most_home_runs[HOME_RUNS] else most_home_runs
    total_attendance_in_1999 += int(team[ATTENDANCE]) if team[YEAR] == 1999 else 0

    win_rate = team[GAMES_WON] / team[GAMES_PLAYED]
    lowest_win_rate_but_won = team if win_rate > (lowest_win_rate_but_won[GAMES_WON] / lowest_win_rate_but_won[GAMES_PLAYED]) and team[WON_WS] > 0 else lowest_win_rate_but_won
    highest_win_rate_but_lost = team if win_rate < (highest_win_rate_but_lost[GAMES_WON] / highest_win_rate_but_lost[GAMES_PLAYED]) and team[WON_WS] == 0 else highest_win_rate_but_lost


print(f'The team with the most home runs was {most_home_runs[TEAM]}!')
print(f'The total attendance of all games in 1999 was {total_attendance_in_1999}!')
print(f'The team with the lowest percentage of wins but won the world series in a season was {lowest_win_rate_but_won[TEAM]}.')
print(f'The team with the highest percentage of wins but lost the world series in a season was {highest_win_rate_but_lost[TEAM]}.')




