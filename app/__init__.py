from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
import os

db = SQLAlchemy()
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
BASE_URL = '/app'
TEMPLATE_DIRECTORY = f'{BASE_DIRECTORY}/templates'
STATIC_DIRECTORY = f'{BASE_DIRECTORY}/static'

def create_app(env=None) -> Flask:
    '''Create the Flask application and bind the sqlalchemy objects'''
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object( config_by_name[ env or 'Test' ])
    Bootstrap(app)
    db.init_app(app)
    register_routes(app)

    database_cli = AppGroup('database')

    @database_cli.command('init')
    def init_database():
        db.create_all()

    app.cli.add_command(database_cli)
    return app
