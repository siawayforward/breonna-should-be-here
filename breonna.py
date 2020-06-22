from datetime import date, timedelta

death = date(2020, 3, 13)
death_str = death.strftime('%B %d, %Y')
days_since_death = (date.today() - death).days

hashtags = ' #BlackLivesMatter #BlackWomenMatter'

status_updates = ['Good morning, @LMPD. It has been {} days since Breonna Taylor died.' 
'Arrest your brethren who murdered her.'.format(days_since_death),
'Don\'t forget, it has been {} days since Breonna Taylor died. Her killers still roam free. '
'@LMPD, please arrest the officers that killed her.'.format(days_since_death),
'Arrest the officers who murdered Breonna Taylor. Charge the officers who murdered Breonna Taylor. '
'Convict the officers who murdered Breonna Taylor.',
'Breonna Taylor died on {}. Her killers have not been arrested, charged, or convicted.'.format(death_str),
'Breonna Taylor had dreams of having a great job and family. '
'She is not doing that, but her killers get to live life. @LMPD, do better',
'Breonna Taylor has a law named after her, but she has not received justice. Make it make sense!'
]