from datetime import datetime
import os

from sqlalchemy import Column, Integer, String, create_engine, Sequence
from sqlalchemy.orm import declarative_base

path_to_db = os.path.dirname(os.path.realpath(__file__)) + f"/bets_{datetime.date(datetime.today())}/"
engine = create_engine(f'sqlite:////{path_to_db}')

Base = declarative_base()


class Bets(Base):
    __tablename__ = 'bets'
    user = Column(String, primary_key=True)
    bet = Column(String)

    def __repr__(self):
        return "<Bets(user='%s', bet='%s')>" % ( self.user, self.bet)

class Teams(Base):
    __tablename__ = "teams"
    _id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    host = Column(String)
    guest_id = Column(Integer)
    guest = Column(String)
        

Base.metadata.create_all(engine)
