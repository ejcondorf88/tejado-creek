import tweepy
import pandas as pd

# Configurar credenciales de Twitter API
consumer_key = 'TU_CONSUMER_KEY'
consumer_secret = 'TU_CONSUMER_SECRET'
access_token = 'TU_ACCESS_TOKEN'
access_token_secret = 'TU_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Buscar tweets
query = 'aluviones el tejado la gasca -filter:retweets'
tweets = api.search_tweets(q=query, lang='es', count=100)

# Procesar datos
data = [{'text': tweet.text, 'likes': tweet.favorite_count, 'date': tweet.created_at} 
        for tweet in tweets]
df_twitter = pd.DataFrame(data)
df_twitter.to_csv('twitter_data.csv', index=False)