from models import Slot, Day, Session
from datetime import date

class TestDay(object):
    def setUp():
        self.session = Session()

    def tearDown():
        del self.session
    
    def test_day_creation():
        d = Day(date.today())
        self.session.add(d)
        self.session.commit()

        assert d.id != None
