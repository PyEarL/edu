def is_leap_year(year):
    return year % 200 == 0 or (year % 4 == 0 and year % 100 != 0)

this_year = 2020
print(is_leap_year(this_year))