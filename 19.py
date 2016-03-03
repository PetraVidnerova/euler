import datetime

d = datetime.datetime(1901,1,1)
stop = datetime.datetime(2000,12,31)

count = 0 
while d < stop:
#    print(d.weekday()," -- ", d)
    if d.weekday() == 6 and d.day == 1:
        count+= 1
    d += datetime.timedelta(days=1)
    
print(count)
