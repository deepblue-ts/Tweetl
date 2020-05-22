## Tweetl
By using tweetl, you can simplify the steps from getting tweets to pre-processing it.
If you have'nt got twitter API, you can get it [here](https://developer.twitter.com/en).

## Installation
```
pip install tweetl
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
#### By target name
You can collect tweets of the target if you use 'get_tweets_target' method and set the target's name not inclueded '@'. Then it returns collected tweets as DataFrame type.
```
# get tweets of @Deepblue_ts
df_target = tweet_getter.get_tweets_target("Deepblue_ts")
df_target.head()
```
<img width="939" alt="スクリーンショット 2020-05-22 14 33 39" src="https://user-images.githubusercontent.com/37981348/82634800-b27fa480-9c39-11ea-9420-8952717823fb.png">

#### By any keyword
You can also get tweets about any keyword if you use 'get_tweets_keyword' method and set any keyword.
```
# get tweets about 'deep learning'
df_keyword = tweet_getter.get_tweets_keyword("deep learning")
```

## Author
deepblue

## License
This software is released under the MIT License, see LICENSE.
