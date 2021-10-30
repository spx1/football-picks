from flask import Flask
APP_NAME = 'health'

def register_routes(app : Flask):
    from .controller import api
    app.register_blueprint(api)