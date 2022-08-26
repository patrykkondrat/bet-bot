from typing import List
from db_init import engine, Bets, Teams
from sqlalchemy import or_
from sqlalchemy.sql import select, update, exists
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from sqlalchemy.exc import IntegrityError

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
        self.id = 1
        self.host_id = 1
        self.host: str = ""
        self.guest_id = 2
        self.guest: str = ""

    def push(self):
        session.rollback()
        ins = Teams(_id=self.id, host_id=self.host_id, host=self.host, guest_id=self.guest_id, guest=self.guest)
        session.add(ins)
        session.commit()

    def set_host_team(self, _host_name):
        self.host = _host_name
        session.rollback()
        print(_host_name)
        if self.guest != "" and self.host != "":
            self.push()
        else:
            print("bez pushu")

    def set_guest_team(self, _guest_name):
        self.guest = _guest_name
        session.rollback()
        print(_guest_name)
        if self.guest != "" and self.host != "":
            self.push()
        else:
            print("bez pushu")
    
    def show_teams(self) -> None:
        pass



if __name__ == "__main__":
    team = TeamServices()
    team.set_host_team("siema")
    team.set_guest_team("siemanko")

