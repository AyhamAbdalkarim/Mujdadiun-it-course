from datetime import date, datetime, timedelta

today = date.today()
print(today, today.year)

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))

later = now + timedelta(days=7)
print("in one week:", later.date())
