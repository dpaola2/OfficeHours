from sqlalchemy import *
from migrate import *

meta = MetaData()

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    slots = Table('slots', meta, autoload = True)

    reserved = Column('reserved', Boolean)
    reserved_by = Column('reserved_by', String(50))
    skype = Column('skype', String(50))
    email = Column('email', String(50))

    reserved.create(slots)
    reserved_by.create(slots)
    skype.create(slots)
    email.create(slots)

def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    slots = Table('slots', meta, autoload = True)
    
    slots.c.email.drop()
    slots.c.skype.drop()
    slots.c.reserved_by.drop()
    slots.c.reserved.drop()
