import os

from sqlalchemy import Column, String, Integer, create_engine, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine(os.environ.get('DATABASE_URL', 'sqlite:///:memory:'), echo = True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key = True)
    date = Column(Date)

    def __init__(self, date):
        self.date = date

    def __repr__(self):
        return "<Day %s>" % str(self.date)

class Slot(Base):
    __tablename__ = 'slots'
    id = Column(Integer, primary_key = True)
    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Day", backref = backref('slots', order_by=id))

    def __init__(self, day):
        self.day = day

    def __repr__(self):
        return "<Slot %s for day: %s>" % (self.id, str(self.day.date))
    
