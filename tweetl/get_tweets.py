import tweepy
import pandas as pd

class GetTweet:
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, proxy=None):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        if proxy:
            self.api = tweepy.API(auth, wait_on_rate_limit = True, proxy=proxy)
        else:
            self.api = tweepy.API(auth, wait_on_rate_limit = True, retry_count=5)

    # get Target's tweets
    def get_tweets_target(self, target):
        tweets = {"tweet_id": [], "created_at": [], "text": [], "favorite_count": [], "retweet_count": []}
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name = target, exclude_replies = True).items():
            tweets["tweet_id"].append(tweet.id)
            tweets["created_at"].append(tweet.created_at)
            tweets["text"].append(tweet.text)
            tweets["favorite_count"].append(tweet.favorite_count)
            tweets["retweet_count"].append(tweet.retweet_count)

        return pd.DataFrame(tweets)

    # search for keywords
    def get_tweets_keyword(self, keyword):
        tweets = {
            "tweet_id": [],
            "created_at": [],
            "screen_name": [],
            "user_name": [],
            "user_description": [],
            "followers_count": [],
            "following_count": [],
            "text": [],
            "favorite_count": [],
            "retweet_count": []
        }
        for tweet in tweepy.Cursor(self.api.search, q=keyword, include_entities=True, tweet_mode='extended', lang='ja').items():
            tweets["tweet_id"].append(tweet.id)
            tweets["created_at"].append(tweet.created_at)
            tweets["screen_name"].append(tweet.user.screen_name)
            tweets["user_name"].append(tweet.user.name)
            tweets["user_description"].append(tweet.user.description)
            tweets["followers_count"].append(tweet.user.followers_count)
            tweets["following_count"].append(tweet.user.friends_count)
            tweets["text"].append(tweet.full_text)
            tweets["favorite_count"].append(tweet.favorite_count)
            tweets["retweet_count"].append(tweet.retweet_count)

        return pd.DataFrame(tweets)
