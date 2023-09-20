from datetime import datetime

current_time = datetime.now()
utc_time = datetime.utcnow()
end_of_month = datetime(2023,9,30,23,59)
d = datetime.strptime("22 may 2023 19:30", "%d %B %Y %H:%M")

print(current_time)
print(utc_time)
#datetime table in Google
print(end_of_month.strftime("%A"))
print(end_of_month.year)

print(end_of_month.strftime("%Y %B %d" ))
print(d)