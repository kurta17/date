from datetime import datetime

current_time = datetime.now()
utc_time = datetime.utcnow()
end_of_month = datetime(2023,9,30,23,59)
d = datetime.strptime("22 may 2023 19:30", "%d %B %Y %H:%M")
c = d.isoformat()
new_date = datetime.fromisoformat(c)

# print(current_time)
# print(utc_time)
#datetime table in Google
# print(end_of_month.strftime("%A"))
# print(end_of_month.year)

# print(end_of_month.strftime("%Y %B %d" ))
# print(c)
# print(new_date)

# print(datetime.now().timestamp())
# print(datetime.fromtimestamp(1200000000))

# print(datetime.now().replace(year = 2004).weekday())
# print((datetime.now() - datetime(2023,9,19)).total_seconds())
total_sec = (datetime(2023,9,21,6,6) - datetime(2023,9,20,18,32)).total_seconds()
print(total_sec)
print(datetime(2023,9,21,6,6) - datetime(2023,9,20,18,32))

