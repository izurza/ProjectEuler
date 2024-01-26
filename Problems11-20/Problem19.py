## Problem 19
from datetime import date, timedelta

def counting_sundays(fy, ly):
    day = date(fy,1,1)
    count =0
    while day.year!=ly+1:
        print(day)
        if day.day == 1 and day.weekday()==6:
            count +=1
        day += timedelta(days=1)
    return count