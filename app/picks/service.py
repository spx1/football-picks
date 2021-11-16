from typing import List
from .model import CTeam
from app import db
from bs4 import BeautifulSoup


URL="https://www.vegasinsider.com/nfl/matchups/matchups.cfm/week/{week}/season/{year}"

def scrap(file: str):
    with open(file,"rt") as f:
        soup = BeautifulSoup( f.read() )
        table = soup.find("table",class_='nfl-matchups')
        for tr in table.tbody.find_all("tr"):
            tds = tr.find_all('td')
            if len(tds) > 2:
                away = tds[0].find('div',style='font-weight: bold;').string
                home = tds[2].find('div',style='font-weight: bold;').string
                print(f'{away} @ {home}')


def init_app():
    scrap('/home/will/documents/projects/football-picks/data/index.html?Year=2021&Week=10')

class TeamService:
    @staticmethod
    def getTeams() -> List[CTeam]:
        return CTeam.query.order_by(CTeam.nickname).all()