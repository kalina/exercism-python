from datetime import date
import calendar
c = calendar.Calendar(firstweekday=calendar.SUNDAY)
num = {'1st':1, '2nd':2, '3rd':3, '4th':4, '5th':5, 'teenth':'', 'last':'' }

def meetup_day(year, month, day, number):

    monthcal = c.monthdatescalendar(year, month)
    dow = getattr(calendar, day.upper())
    dates = [day for week in monthcal for day in week if \
                day.weekday() == dow and \
                day.month == month]
    if number == 'last':
        meetup_date = dates[-1]
    elif number == 'teenth':
        for dom in dates:
            if dom.day >=13 and dom.day <= 19:
                meetup_date = dom
    else:
        meetup_date = dates[num[number]-1]
    return meetup_date
