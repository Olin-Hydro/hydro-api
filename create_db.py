# Create HydroDB database
import os
import sqlite3
import datetime as dt
from api import PhModel, db


# Create initial test data
now = dt.datetime.utcnow()
PH =  [
    {"timestamp": now, "ph": 6.1, "ph_raw": "temp:22.52, resistance:302"},
    {"timestamp": now, "ph": 7, "ph_raw": "temp:22.4, resistance:300"},
    {"timestamp": now, "ph": 5.6, "ph_raw": "temp:22.1, resistance:303"}
]

# Delete the database if it exists
if os.path.exists('HydroDB.db'):
    os.remove('HydroDB.db')

# Create the database
db.create_all()

# Add initial test data
for log in PH:
    l = Ph(timestamp=log['timestamp'], ph=log['ph'], ph_raw=log['ph_raw'])
    db.session.add(l)

# Save changes
db.session.commit()