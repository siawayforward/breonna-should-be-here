from datetime import date, timedelta
from Angel import Angel

death = date(2020, 3, 13)
death_str = death.strftime('%B %d, %Y')
days_since_death = (date.today() - death).days

hashtags = ' #BlackLivesMatter #BlackWomenMatter'

search_terms = ['BreonnaTaylor', 'Breonna Taylor', 'BREONNA TAYLOR']


Breonna = Angel('breonna-updates.txt')
print(Breonna.name)
print(Breonna.ascension_date)
print(Breonna.days_since)
print(Breonna.hashtags)

