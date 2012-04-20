import os

from sqlalchemy import Column, String, Integer, create_engine, Date, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

engine = create_engine(os.environ.get('DATABASE_URL'), echo = True)
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

    @property
    def label(self):
        return self.date.strftime("%a %B %d")

    @staticmethod
    def days_ahead(limit):
        sess = Session()
        return sess.query(Day).order_by(Day.date).limit(limit).all()

class Slot(Base):
    __tablename__ = 'slots'
    id = Column(Integer, primary_key = True)
    day_id = Column(Integer, ForeignKey('days.id'))
    day = relationship("Day", backref = backref('slots', order_by=id))
    when = Column(DateTime, unique = True)

    def __init__(self, day, when):
        self.day = day
        self.when = when

    def __repr__(self):
        return "<Slot %s for day: %s>" % (self.id, str(self.day.date))

    @property
    def label(self):
        return self.when.strftime("%I:%M %p")

    @staticmethod
    def from_datetime(when):
        sess = Session()
        day = sess.query(Day).filter_by(date=when.date()).scalar()
        if day is None:
            day = Day(when.date())
            sess.add(day)

        slot = Slot(day, when)
        sess.add(slot)
        sess.commit()
        return slot
