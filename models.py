from pydantic import BaseModel


class TweetRequest(BaseModel):
    username: str
    tweet_count: int = 5
