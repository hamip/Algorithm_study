# https://www.hackerrank.com/challenges/write-a-function/problem

# Write a function

def is_leap(year):
    leap = False
    
    # The year can be evenly divided by 4, is a leap year, unless:
    if year % 4 == 0:
        leap = True
        # The year can be evenly divided by 100, it is NOT a leap year, unless:
        if year % 100 == 0:
            leap = False
            # The year is also evenly divisible by 400. Then it is a leap year.
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))
