#!/usr/bin/env python3
"""
App file.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    The config class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAUT_TIMEZONE = 'UTC'

config = Config()
app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@app.route('/')
def index():
    """
    Default root
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)