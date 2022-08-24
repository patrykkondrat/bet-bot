from typing import List
from db_init import engine, Bets, Teams
from sqlalchemy.sql import select, update
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from sqlalchemy.exc import IntegrityError

Session = sessionmaker(bind=engine)
session = Session()

# def is_valid_bet(_bet) -> bool:
    # print(Bets.__table__)
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
    _teams: dict = {"host_id": 1, "host_name": "", "guest_id": 2, "guest_name": "" }
    
    def set_host_team(self, _host_name):
        try:
            ins = Teams(host=_host_name)
            session.add(ins)
            session.commit()
        except:
            print("lipa")
    
    def set_guest_team(self, _guest_name):
        try:
            ins = Teams(guest=_guest_name)
            session.add(ins)
            session.commit()
        except:
            print("lipa")