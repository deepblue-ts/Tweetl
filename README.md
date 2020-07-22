## Tweetl
By using tweetl, you can simplify the steps from getting tweets to pre-processing them.
If you don't have twitter API key, you can get it [here](https://developer.twitter.com/en).

This package help you to ・・・
+ get tweets with the target name and any keywords.
+ pre-processes the following list.
  + remove hashtags, URLs, pictographs, mentions, image strings and RT.
  + unify characters (uppercase to lowercase, halfwidth forms to fullwidth forms).
  + replace number to zero.
  + remove duplicates (because they might be RT.)

## Installation
```
pip install Tweetl
```
## Usage
### Getting Tweets
Create an instance of the 'GetTweet' Class.
```
import tweetl

# your api keys
consumer_api_key = "xxxxxxxxx"
consumer_api_secret_key = "xxxxxxxxx"
access_token = "xxxxxxxxx"
access_token_secret = "xxxxxxxxx"

# create an instance
tweet_getter = tweetl.GetTweet(
                    consumer_api_key,
                    consumer_api_secret_key, 
                    access_token, 
                    access_token_secret
                )
```
#### With target name
You can collect tweets of the target if you use 'get_tweets_target' method and set the target's name not inclueded '@'. Then it returns collected tweets as DataFrame type. And you can specify the number of tweets. The default is 100.
```
# get 1000 tweets of @Deepblue_ts
df_target = tweet_getter.get_tweets_target("Deepblue_ts", 1000)
df_target.head()
```
<img width="939" alt="スクリーンショット 2020-05-22 14 33 39" src="https://user-images.githubusercontent.com/37981348/82634800-b27fa480-9c39-11ea-9420-8952717823fb.png">

#### With any keywords
You can also get tweets about any keywords if you use 'get_tweets_keyword' method and set any one. And you can specify the number of tweets. The default is 100.
```
# get 1000 tweets about 'deep learning'
df_keyword = tweet_getter.get_tweets_keyword("deep learning", 1000)
```

### Cleansing Tweets
Create an instance of the 'CleansingTweets' Class. And using 'cleansing_df' method, you can pre-processing tweets. You can select columns that you want to cleanse. The default is only text-colmn.

```
# create an instance
tweet_cleanser = tweetl.CleansingTweets()
cols = ["text", "user_description"]
df_clean = tweet_cleanser.cleansing_df(df_keyword, subset_cols=cols)
```

## Author
[deepblue](https://deepblue-ts.co.jp/)

## License
This software is released under the MIT License, see [LICENSE](https://github.com/deepblue-ts/Tweetl/blob/master/LICENSE).
