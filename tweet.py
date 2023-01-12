import tweepy
import keys
from odds_scraper import predictions


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str):
    api.update_status(message)
    print('Tweeted Successfully')


if __name__ == '__main__':
    api = api()
    tweet(api, predictions())
