import time
import datetime

current_time = datetime.datetime.now()
print("a) Current date and time:", current_time)

current_year = current_time.year
print("b) Current Year:", current_year)

month = current_time.strftime("%B")
print("c) Month of the year:", month)

week_number = current_time.strftime("%U")
print("d) Week number of the year:", week_number)

weekday = current_time.strftime("%A")
print("e) Weekday of the week:", weekday)

day_of_year = current_time.strftime("%j")
print("f) Day of year:", day_of_year)

day_of_month = current_time.strftime("%d")
print("g) Day of the month:", day_of_month)

day_of_week = current_time.strftime("%w")
print("h) Day of week (0 - Sunday, 1 - Monday, ...):", day_of_week)
