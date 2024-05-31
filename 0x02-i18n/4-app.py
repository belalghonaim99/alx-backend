#!/usr/bin/env python3
""" Module for trying out Babel i18n """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration Class for Babel"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ best match language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Default route

    Returns:
        str: template 4-index.html
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
