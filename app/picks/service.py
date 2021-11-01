from typing import List
from .model import CTeam
from app import db

def init_app():
    db.session.add( CTeam(city="New York",nickname="Giants") )
    db.session.add( CTeam(city="New York",nickname="Jets") )
    db.session.add( CTeam(city="Kansas City", nickname="Chiefs") )
    db.session.commit()

class TeamService:
    @staticmethod
    def getTeams() -> List[CTeam]:
        return CTeam.query.order_by(CTeam.nickname).all()