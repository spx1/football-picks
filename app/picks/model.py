from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app import db

class CTeam(db.Model):
    __tablename__ = 'teams'
    id = Column(Integer,primary_key=True)
    city = Column(String(50))
    nickname = Column(String(50))

class CGame(db.Model):
    __tablename__ = 'games'
    id = Column(Integer,primary_key=True)
    week = Column(Integer)
    date = Column(Date)
    home_id = Column(Integer,ForeignKey('teams.id'))
    home = db.relationship('CTeam', foreign_keys=home_id)
    away_id = Column(Integer,ForeignKey('teams.id'))
    away = db.relationship('CTeam', foreign_keys=away_id)

class CPick(db.Model):
    __tablename__ = 'picks'
    id = Column(Integer,primary_key=True)
    game_id = Column(Integer,ForeignKey('games.id'))
    game = db.relationship('CGame')
    team_id = Column(Integer,ForeignKey('teams.id'))
    team = db.relationship('CTeam')

