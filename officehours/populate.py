from models import *
from datetime import *

now = datetime(year=2012, month=4, day=20, hour=16, minute=0)
num_days = 7
num_slots = 4


for i in range(num_days):
    for j in range(num_slots):
        when = now + timedelta(days=i, hours=j)
        Slot.from_datetime(when)
