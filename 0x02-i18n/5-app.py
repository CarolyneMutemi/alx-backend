#!/usr/bin/env python3
"""
App file.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    """
    The config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAUT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}
    }


def get_user():
    """
    Returns a dictionary depending on the id passed to login_as parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Executed before any app functions.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Gets the preferred locale.
    """
    lang = request.args.get('locale')
    user_locale = None
    if lang in app.config["LANGUAGES"]:
        return lang
    if g.user:
        user_locale = g.user.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Default root
    """
    if not g.user:
        message = gettext("You are not logged in.")
        username = ''
    else:
        message = gettext("You are logged in as")
        username = f" {g.user.get('name')}."
    return render_template('5-index.html', message=message, username=username)


if __name__ == '__main__':
    app.run(debug=True)
