from datetime import date, timedelta
from Angel import Angel

death = date(2020, 3, 13)
death_str = death.strftime('%B %d, %Y')
days_since_death = (date.today() - death).days

Breonna = Angel('breonna-updates.txt')
print(Breonna.name)
print(Breonna.ascension_date)
print(Breonna.hashtags)
print(Breonna.updates)

