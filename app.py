from flask import Flask, render_template, request
import json
from data_model import DB, User, Tweet
from twitter import upsert_user
from obtain_user import get_user_and_tweets


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def landing():
        DB.drop_all()
        DB.create_all()
        DB.session.commit()
        with open('templates/landing.json') as f:
            args = json.load(f)
        return render_template('base.html', **args)

    # @app.route('/add_user', methods=['GET'])
    # def add_user():
    #     twitter_handle = request.args['twitter_handle']
    #     upsert_user(twitter_handle)
    #     return 'Insert Successful'

    @app.route('/user', methods=['GET'])
    def add_user():
        twitter_handle = request.args['twitter_handle']
        get_user_and_tweets(twitter_handle)
        return 'User added'

    return app


if __name__ == "__main__":
    create_app().run()
