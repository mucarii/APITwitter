from fastapi import FastAPI, HTTPException
from models import TweetRequest
from twitter_api import get_user_timeline_tweets

app = FastAPI()


@app.get("/", summary="Root endpoint", description="Bem-vindo ao Twitter API consumer")
def read_root():
    return {"message": "Welcome to the Twitter API consumer"}


@app.post(
    "/tweets",
    summary="Pegar Tweets de um Usuário",
    description="Recuperar uma lista de tweets de um usuário especificado.",
)
def get_user_timeline(request: TweetRequest):
    try:
        tweets = get_user_timeline_tweets(request.username, request.tweet_count)
        return tweets
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
