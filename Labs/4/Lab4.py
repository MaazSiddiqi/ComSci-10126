numDays = int(input("Enter the number of days in the month: "))
dayOfWeek = int(input("Enter the starting day of the month (0 = Su, 1= Mo, ..., 6=Sa): "))

print(' Su Mo Tu We Th Fr Sa ')
print(' ' * dayOfWeek * 3, end='')

for i in range(1,numDays+1):
    print('{:3}'.format(i), end='')

    if dayOfWeek == 6:
        print("")
        dayOfWeek = 0
    else:
        dayOfWeek += 1

    numDays += 1

