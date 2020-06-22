from datetime import date, timedelta
from Angel import Angel

death = date(2020, 3, 13)
death_str = death.strftime('%B %d, %Y')
days_since_death = (date.today() - death).days

hashtags = ' #BlackLivesMatter #BlackWomenMatter'

search_terms = ['BreonnaTaylor', 'Breonna Taylor', 'BREONNA TAYLOR']


Breonna = Angel('breonna-updates.txt')
for line in Breonna.updates:
    print(line, '\n')