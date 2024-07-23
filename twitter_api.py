import tweepy
import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Carregar variáveis de ambiente
load_dotenv()

# Substitua pelos valores obtidos do arquivo .env
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


def authenticate_twitter_app():
    auth = tweepy.OAuth1UserHandler(
        API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)
    return api


def get_user_timeline_tweets(username: str, tweet_count: int):
    tweet_count = min(tweet_count, 200)  # Limitar a 200 tweets
    api = authenticate_twitter_app()
    try:
        tweets = api.user_timeline(
            screen_name=username, count=tweet_count, tweet_mode="extended"
        )
        return [
            {"user": tweet.user.screen_name, "text": tweet.full_text}
            for tweet in tweets
        ]
    except tweepy.TweepError as e:
        raise HTTPException(status_code=500, detail=f"Twitter API error: {e}")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {e}"
        )
