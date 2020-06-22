import time
from datetime import datetime
import tweepy
import breonna

class Breonna_API:
    
    def __init__(self, **kwargs):
        self.define_API(**kwargs)
        self.me = self.api.me()
        self.search = ['BreonnaTaylor', 'Breonna Taylor', 'BREONNA TAYLOR']
        self.tweet_ct = 500
       
    def define_API(self, **kwargs):
        #add API auth keys in order
        self.consumer_key = kwargs['c_key']
        self.consumer_secret = kwargs['c_secret']
        self.access_key = kwargs['a_key']
        self.access_tkn_secret = kwargs['a_secret']

        #define twitter API and authorization params
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_key, access_tkn_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def tweet_and_retweet(self):
        start = 0
        end = 86400 #total seconds in a day
        current = datetime.now()
        #restart clock everyday
        if current.hour == 0 and current.minute == 0 and current.second == 0:
            start = 0
        try:
            while start <= end:
                for tweet in tweepy.Cursor(self.api.search, self.search).items(self.tweet_ct):
                    if not tweet.favorited:
                        try:
                            print('Tweet Liked and Retweeted')
                            start += 72
                            tweet.favorite()
                            tweet.retweet()
                            time.sleep(72) #to reach 1200 per day at most because we want to post 1200 tweets too
                        except tweepy.TweepError as e: pass
                        except StopIteration:
                            break
        except start > 86400: pass
                                   
    def post_scheduled_tweets(self):
        for tweet in breonna.status_updates:
            try:
                print('Tweet posted')
                self.api.update_status(tweet + breonna.hashtags)
                time.sleep(72)
            except tweepy.TweepError as e: pass
            except StopIteration:
                break

    def get_user(self):
        self.user = api.me()
        return self.user

    def get_followers(self):
        for follower in tweepy.Cursor(api.followers).items():
            print(follower.name)


if __name__ == '__main__':
    login = Breonna_API()
    login.post_scheduled_tweets()
    login.tweet_and_retweet()
