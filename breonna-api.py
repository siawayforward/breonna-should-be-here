import time
from datetime import datetime
import tweepy
from Angel import Angel

class Breonna_API:
    
    def __init__(self, cred_file, angel_file=None):
        if angel_file: self.Breonna = Angel(angel_file)
        self.define_API(cred_file)
        self.me = self.api.me()
        self.search = self.Breonna.search
        self.tweet_ct = 500
       
    def define_API(self, cred_file):
        #add API auth keys in order
        try:
            with open(cred_file, 'r') as file:
                self.consumer_key = file.readline().split(',')[1].strip()
                self.consumer_secret = file.readline().split(',')[1].strip()
                self.access_key = file.readline().split(',')[1].strip()
                self.access_tkn_secret = file.readline().split(',')[1].strip()
        except: pass

        #define twitter API and authorization params
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_tkn_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def tweet_and_retweet(self):
        current = datetime.now()
        start = 0
        #restart clock everyday
        try:
            for tweet in tweepy.Cursor(self.api.search, self.search).items(self.tweet_ct):
                if not tweet.favorited and not tweet.retweeted:
                    try:
                        start += 72
                        tweet.favorite()
                        tweet.retweet()
                    except tweepy.TweepError as e: continue
                    except StopIteration: break
                print('Tweet Liked and Retweeted', start)
                time.sleep(72) #to reach 1200 per day at most because we want to post 1200 tweets too
        except tweepy.RateLimitError as e: StopIteration
                                   
    def post_scheduled_tweets(self):
        for tweet in self.Breonna.status_updates:
            try:
                print('Tweet posted')
                self.api.update_status(tweet + self.Breonna.hashtags)
                time.sleep(72)
            except tweepy.TweepError as e: break
            except StopIteration:
                break

    def get_user(self):
        self.user = api.me()
        return self.user

    def get_followers(self):
        for follower in tweepy.Cursor(api.followers).items():
            print(follower.name)


if __name__ == '__main__':
    login = Breonna_API('run.txt', 'breonna-updates.txt')
    login.post_scheduled_tweets()
    login.tweet_and_retweet()
