from flask import Flask, Blueprint, render_template
from app import STATIC_DIRECTORY, TEMPLATE_DIRECTORY, BASE_URL
from . import APP_NAME

api = Blueprint(
    name = f'{APP_NAME}',
    import_name = __name__,
    static_folder = f'{STATIC_DIRECTORY}',
    template_folder = f'{TEMPLATE_DIRECTORY}',
    url_prefix = f'{BASE_URL}/{APP_NAME}'
)

@api.route('status')
def status():
    return 'Picks is running successfully'