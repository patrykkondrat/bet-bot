from typing import List
from db_init import engine, Bets 
from sqlalchemy.sql import select, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table
from tabulate import tabulate

con = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

# def is_valid_bet(_bet) -> bool:
    # print(Bets.__table__)

def make_bet(user_id, _user, _bet):
    ins = Bets(id=user_id, user=_user, bet=_bet)
    session.add(ins)
    session.commit()


def show_table(plot=True) -> List:
    res = con.execute(select(Bets))
    out = []
    for i in res:
        out.append(list(i))
    if plot == True:
        print(tabulate(out, headers=Bets.__table__.columns.keys(), tablefmt="fancy_grid", showindex="never"))
    return out

if __name__ == "__main__":
    # is_valid_bet(2)
    make_bet(3, "Dorota", "1")
    Bets.__table__
    print(show_table())