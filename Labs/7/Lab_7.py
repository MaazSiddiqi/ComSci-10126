def averagePref(L,x):
    total = 0
    for i in range(x):
        try:
            total += L[i]
        except IndexError:
            break

    try:
        avg = total / x
        return avg
    except ZeroDivisionError:
        return -1


print(averagePref([1.0, 6.3, 2.3, 7.3, 2.0], 1))
print(averagePref([1.0, 6.3, 2.3, 7.3, 2.0], 0))
print(averagePref([1.0, 6.3, 2.3, 7.3, 2.0], 9))


