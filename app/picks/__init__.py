from flask import Flask
APP_NAME = 'picks'

def register_routes(app : Flask):
    from .controller import api
    app.register_blueprint(api)
    