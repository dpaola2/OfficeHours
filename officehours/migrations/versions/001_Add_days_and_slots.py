from sqlalchemy import *
from migrate import *

meta = MetaData()

day = Table(
    'days', meta,
    Column('id', Integer, primary_key = True),
    Column('date', Date, unique = True)
)

slot = Table(
    'slots', meta,
    Column('id', Integer, primary_key = True),
    Column('day_id', Integer, ForeignKey('days.id')),
    Column('when', DateTime, unique = True)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    day.create()
    slot.create()

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    slot.drop()
    day.drop()
