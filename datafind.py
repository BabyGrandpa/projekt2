import datetime as dt

#returnere dato med format eksemple 1
def get_date1():
    date = dt.date.today()
    date_c = date.strftime('%d/%m/%Y')
    return date_c

#returnere dato med format eksemple 2
def get_date2():
    date = dt.date.today()
    date_c = date.strftime('%d/%m/%y')
    return date_c

#returnere tid med format eksemple 1
def get_time1():
    time = dt.datetime.now()
    time_c = time.strftime('%H:%M')
    return time_c

#returnere tid med format eksemple 2
def get_time2():
    time = dt.datetime.now()
    time_c = time.strftime('%h:%m')
    return time_c

print("Date format example 1",get_date1())
print("Date format example 2",get_date2())
print("Time format example 1",get_time1())
print("Time format example 2",get_time2())