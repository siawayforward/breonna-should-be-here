from datetime import date, timedelta
from Angel import Angel

death = date(2020, 3, 13)
death_str = death.strftime('%B %d, %Y')
days_since_death = (date.today() - death).days

Breonna = Angel('breonna-updates.txt')
print('name:', Breonna.name)
print('date:', Breonna.ascension_date)
print('tags:', Breonna.hashtags)
print('search terms:', Breonna.search)

