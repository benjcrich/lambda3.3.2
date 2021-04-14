from flask import Flask, render_template, request
import json
from data_model import DB
from obtain_user import get_user_and_tweets
from ml import predict_most_likely_author


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    # Landing page for our web app
    @app.route('/')
    def landing():
        return render_template('landing.html')

    # Contains the input for a user
    @app.route('/user')
    def user():
        return render_template('user.html')

    # Adds the user and displays the success message
    @app.route('/add_user', methods=['GET'])
    def add_user():
        twitter_handle = request.args['twitter']
        get_user_and_tweets(twitter_handle)
        return 'User added successfully'

    # Predicts which user most likely tweeted the string given.
    @app.route('/predict_author', methods=['GET'])
    def predict_author():
        user1 = 'cher'
        user2 = 'elonmusk'
        tweet_to_classify = request.args['tweet_to_classify']
        return predict_most_likely_author((tweet_to_classify, [user1, user2]))

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'Database Reset'

    @app.route('/test')
    def test():
        return 'Test Successful'

    return app


if __name__ == "__main__":
    create_app().run()
