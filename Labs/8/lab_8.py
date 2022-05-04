def makeDicts():
    incomeDict = dict()
    countryDict = dict()
    countryList = []
    gdpList = []
    initialList = []
    with open('lab8.txt', 'r') as f:
        for Line in f:
            line = Line.upper().strip().split(':')
            countryList.append(line[0])
            gdpList.append(line[1])
            initial = line[0][0]
            initialList.append(initial)
    for i in range(len(countryList)):
        incomeDict[countryList[i]] = gdpList[i]
        if initialList[i] not in countryDict:
            countryDict[initialList[i]] = set()
        countryDict[initialList[i]].add(countryList[i])

    return (incomeDict, countryDict)


def main():
    incomeDict, countryDict = makeDicts()
    while True:
        inp = input('Enter an initial or country name: ').upper()

        if inp == 'DONE':
            break
        elif inp in countryDict:
            print(f'These countries start with {inp}: {countryDict[inp]}')
        elif inp in incomeDict:
            print(f'{inp} has per capita GDP of {incomeDict[inp]}')
        else:
            print('Error, invalid input')
            continue


main()



