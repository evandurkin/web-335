# Author: Evan Durkin
# Title: Exercise 9.2
# Date: 12/18/2021

import datetime
import pprint
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
print(client)

client = MongoClient("localhost", 27017)
db = client.web335
pprint.pprint(db.users.find_one())

client = MongoClient("localhost", 27017)
db = client.web335
user = {
    "first_name": "Wolfgang",
    "last_name": "Mozart",
    "email": "wmozart@me.com",
    "employee_id": "0000009",
    "date_created": datetime.datetime.utcnow()
}
user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "0000009"}))
