#!/usr/bin/env python3
"""
App file.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """
    Gets the preferred locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Default root
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
