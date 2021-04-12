import requests
import ast

from data_model import DB, User, Tweet


def get_user_and_tweets(username):

    HEROKU_URL = 'https://lambda-ds-twit-assist.herokuapp.com/user/'

    user = ast.literal_eval(requests.get(HEROKU_URL + username).text)

    try:
        if User.query.get(user['twitter_handle']['id']):
            db_user = User.query.get(user['twitter_handle']['id'])
        else:
            db_user = User(id=user['twitter_handle']['id'],
                           name=user['twitter_handle']['username'])
        DB.session.add(db_user)

        for tweet in user['tweets']:
            db_tweet = Tweet(id=tweet['id'], text=tweet['full_text'])
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        raise e
    else:
        DB.session.commit()
