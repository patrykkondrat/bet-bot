from typing import List

from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists, select, update, delete
from tabulate import tabulate

from db_init import Bets, Teams, engine

Session = sessionmaker(bind=engine)
session = Session()

def is_valid_bet(_bet) -> bool:
    return bool(session.query(Teams).filter(or_(Teams.host == _bet, Teams.guest == _bet,Teams.guest_id == _bet,Teams.host_id == _bet)).first())

class BetServices:
    def change_bet(self, _user: str, _bet: str) -> None:
        session.query(Bets).filter(Bets.user == _user).update({Bets.bet: _bet})
        session.commit()

    def make_bet(self, _user, _bet) -> None:
        try:
            ins = Bets(user=_user, bet=_bet)
            session.add(ins)
            session.commit()
        except IntegrityError:
            session.rollback()
            self.change_bet(_user, _bet)
            print("Bet in game")

    def show_table(self, plot=True) -> List:
        con = engine.connect()
        res = con.execute(select(Bets))
        out = []
        for i in res:
            out.append(list(i))
        table = tabulate(out, headers=Bets.__table__.columns.keys(), tablefmt="fancy_grid", showindex="never")
        if plot == True:
            print(table)
        return table

class TeamServices: 
    def __init__(self):   
        self.id: int = 1
        self.host_id: int = 1
        self.host: str = ""
        self.guest_id: int = 2
        self.guest: str = ""
        self.winner: str = ""

    def push(self):
        try:
            ins = Teams(_id=self.id, host_id=self.host_id, host=self.host, guest_id=self.guest_id, guest=self.guest)
            session.add(ins)
        except:
            session.rollback()            
            # session.query(Teams).filter(Teams._id == self.id).delete()
            # ins = Teams(_id=self.id, host_id=self.host_id, host=self.host, guest_id=self.guest_id, guest=self.guest)
        finally:
            session.commit()

    def set_host_team(self, _host_name):
        self.host = _host_name
        if self.guest != "" and self.host != "":
            self.id += 1
            self.push()

    def set_guest_team(self, _guest_name):
        self.guest = _guest_name
        if self.guest != "" and self.host != "":
            self.id += 1
            self.push()

    def set_winner(self, winner):
        self.winner = winner

    def show_teams(self, plot=True) -> None:
        con = engine.connect()
        res = con.execute(select(Teams))
        out = []
        for i in res:
            out.append(list(i))
        table = tabulate(out, headers=Bets.__table__.columns.keys(), tablefmt="fancy_grid", showindex="never")
        if plot == True:
            print(table)
        return table

if __name__ == "__main__":
    team = TeamServices()
    team.set_host_team("siema")
    team.set_guest_team("siemanko")
    team.set_host_team("kolsiemankoo")

