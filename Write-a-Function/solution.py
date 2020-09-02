def is_leap(year):
    leap = False
    if year // 4 == year / 4  and year / 100 != year // 100 or year // 400 == year / 400:
        leap = True
    else:
        leap = False
    return leap

year = int(input())