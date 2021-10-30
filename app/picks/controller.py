from flask import Flask, Blueprint, render_template, redirect, url_for
from app import STATIC_DIRECTORY, TEMPLATE_DIRECTORY, BASE_URL
from . import APP_NAME
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')

api = Blueprint(
    name = f'{APP_NAME}',
    import_name = __name__,
    static_folder = f'{STATIC_DIRECTORY}',
    template_folder = f'{TEMPLATE_DIRECTORY}',
    url_prefix = f'{BASE_URL}/{APP_NAME}'
)

@api.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        message = f'Hello {name}'

    return render_template('index.html', form=form, message=message)

@api.route('status')
def status():
    return 'Picks is running successfully'