import os

from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import declarative_base

count = 0
path_to_db = os.path.dirname(os.path.realpath(__file__)) + f"/bets_{count}/"
engine = create_engine(f'sqlite:////{path_to_db}')

Base = declarative_base()


class Bets(Base):
    __tablename__ = 'bets'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user = Column(String)
    bet = Column(String)

    def __repr__(self):
        return "<Bets(id='%i', user='%s', bet='%s')>" % (self.id, self.user, self.bet)

class Teams(Base):
    __tablename__ = "teams"
    game_id = Column(Integer, primary_key=True)
    host = Column(String)
    guest = Column(String)
        

Base.metadata.create_all(engine)
