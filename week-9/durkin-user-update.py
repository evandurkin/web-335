# Author: Evan Durkin
# Title: Exercise 9.3
# Date: 12/18/2021

from pymongo import MongoClient
import pprint
import datetime
client = MongoClient("localhost", 27017)
db = client.web335
db.users.update_one(
    {"employee_id": "0000009"},
    {
        "$set": {
            "email": "edurkin@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"email": "edurkin@my365.bellevue.edu"}))
