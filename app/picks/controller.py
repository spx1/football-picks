from typing import Dict, List
from flask import Flask, Blueprint, render_template, redirect, url_for
from app import STATIC_DIRECTORY, TEMPLATE_DIRECTORY, BASE_URL
from . import APP_NAME
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, FieldList
from .service import TeamService

class NameForm(FlaskForm):
    name = StringField('What is your name?')
    submit = SubmitField('Submit')

class GameForm(FlaskForm):
    games = FieldList(RadioField(label='Game',choices=['Home Team','None', 'Away Team'],default='None'))
    submit = SubmitField('Submit')

api = Blueprint(
    name = f'{APP_NAME}',
    import_name = __name__,
    static_folder = f'{STATIC_DIRECTORY}',
    template_folder = f'{TEMPLATE_DIRECTORY}',
    url_prefix = f'{BASE_URL}/{APP_NAME}'
)
def get_games() -> List[Dict[str,str]]:
    return [
        {'home':'Kansas City Cheifs','away':'New York Giants'},
        {'home':'New England Patriots','away':'Los Angeles Chargers'},
        {'home':'Philadelphia Eagles','away':'New York Jets'},
        {'home':'Indianapolis Colts','away':'Jacksonville Jaguars'}
    ]
@api.route('/', methods=['GET','POST'])
def index():
    form = GameForm()
    for n,teams in enumerate(get_games(), 1):
        x = form.games.append_entry()
        x.label.text = f'Game {n}'
        x.choices = [teams['home'],'None',teams['away']]

    message = "hello world"
    if form.validate_on_submit():
        selected = []
        for i in form.games:
            print(i.data)
            if i.data != 'None': selected.append( i.data )
        message = 'You selected \r\n {}'.format('\r\n'.join(selected))

    return render_template('index.html', form=form, message=message)

@api.route('/teams', methods=['GET'])
def teams():
    teams = TeamService.getTeams()
    return render_template('teams.html',teams=teams)

@api.route('status')
def status():
    return 'Picks is running successfully'