from typing import List
from db_init import engine, Bets 
from sqlalchemy.sql import select, update
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from sqlalchemy.exc import IntegrityError
con = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

# def is_valid_bet(_bet) -> bool:
    # print(Bets.__table__)

def change_bet(_user, _bet):
    session.query(Bets).filter(Bets.user == _user).update({Bets.bet: _bet})
    session.commit()

def make_bet(user_id, _user, _bet):
    try:
        ins = Bets(id=user_id, user=_user, bet=_bet)
        session.add(ins)
        session.commit()
    except IntegrityError:
        session.rollback()
        # change_bet(_user, _bet)
        print("Bet in game")

# def add_team(name):

# def winners(bet):

def show_table(plot=True) -> List:
    res = con.execute(select(Bets))
    out = []
    for i in res:
        out.append(list(i))
    if plot == True:
        print(tabulate(out, headers=Bets.__table__.columns.keys(), tablefmt="fancy_grid", showindex="never"))
    return out

if __name__ == "__main__":
    make_bet(5, "Dorota5", '2')
    change_bet("Dorota5", "1")
    print(show_table(0))