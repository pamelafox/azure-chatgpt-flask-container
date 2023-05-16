from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import chat  # noqa

    app.register_blueprint(chat.bp)

    return app
