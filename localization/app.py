#!/usr/bin/env python3
"""
Flask application demonstrating string localization with Flask-Babel
"""
from flask import Flask, request, render_template_string
from flask_babel import Babel, _, ngettext

app = Flask(__name__)

def get_locale():
    return request.accept_languages.best_match(['en', 'fr'])

babel = Babel(app, locale_selector=get_locale)

app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'


@app.route('/')
def index():
    """Main route that demonstrates translations"""
    greeting = _("Hello, World!")

    num_messages = 5
    message = ngettext(
        "You have one message",
        "You have %(num)d messages",
        num_messages
    ) % {'num': num_messages}

    welcome = _("Welcome to our application")

    num_files = 1
    file_message = ngettext(
        "%(num)d file processed",
        "%(num)d files processed",
        num_files
    ) % {'num': num_files}

    template = """
    <html>
        <body>
            <h1>{{ greeting }}</h1>
            <p>{{ welcome }}</p>
            <p>{{ message }}</p>
            <p>{{ file_message }}</p>
            <p><small>Current locale: {{ locale }}</small></p>
        </body>
    </html>
    """

    return render_template_string(
        template,
        greeting=greeting,
        welcome=welcome,
        message=message,
        file_message=file_message,
        locale=get_locale()
    )


if __name__ == "__main__":
    app.run(debug=True)
