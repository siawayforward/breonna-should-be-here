# breonna-should-be-here

## Inspired by Breonna Taylor

This is a Twitter bot that periodically retweets and likes any posts reminding the Louisville Metro PD to arrest, charge, and convict the officers who killed Breonna Taylor. This will change back and forth to also reflect positive experience of black people from all parts of the world. It also posts tweets throughout the day with music, authors, pioneers in black culture. All happening within tweeting, liking, and retweeting limits set by Twitter.

`Angel.py` class: can be used to pass a textfile that contains details about the Angel. See below for detailed instructions

In the status updates, the class accounts for anytime a reference to the `ascension date`, or `number of days` since the angel ascended with a format function to allow the display. A variation of this class for people who are still living is in process.

### Instructions

- You will need to host your application on a platform like Netlify or Heroku
- Create Twitter developer account and apply for approval to create applications so that you can generate keys and tokens

A good guide on how to set up an account can be found in the two links below (thanks to the content creators below!):
<https://realpython.com/twitter-bot-python-tweepy/>  
<https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39>  

- Prepare a keys (API and access keys and tokens) file with format shown above to access account  

`keys` textfile for access to account. Do not violate Twitter API access guidelines using the access and secret tokens and keys. They will shut you down. You are able to use this class with a file of keys provided they are in the following order and form (name, value):
> API key, `<value>`
> API secret key, `<value>`
> Access token, `<value>`
> Access token secret, `<value>`

- Prepare an updates file that contains details about the Angel to allow for automation. The textfile `.txt` ordered as follows:  

> `ln 1:` name of Angel  
> `ln 2:` ascension date of Angel  
> `ln 3:` hashtags to add at the end of each status update  
> `ln 4 -> end:` status updates
