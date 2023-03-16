from datetime import date, datetime

today = date.today()
print("Today is: ", today)
print("Day: ", today.day)
print("month: ", today.month)
print("Year: ", today.year)

print(today.strftime("%A,  %dth of %b %y"))

next_year = today.replace(year=today.year + 1)
print(next_year)

difference = abs(next_year - today)

print("only {} days until next year".format(difference.days))

NikolaTesla = date(1856, 7, 10)
NikolaTesla = date.fromisoformat("1856-07-10")
print(NikolaTesla)
print(NikolaTesla.weekday())

now = datetime.now()
print("right now it's: ", now)
print("It's the {}th minute of the {}nd hour of the {}th day of the {}nd month".format(now.minute, now.hour, now.day, now.month))

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
print(chernobyl.strftime("Disaster occured on %A %B %dth, %Y at %X MSD(%Z)"))