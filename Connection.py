import datetime
from pymongo import MongoClient


client = MongoClient()
db = client["Putin"]
collection = db["Trump"]

insertList = {"name": "trump", "vorname": "donald", "alter": 51, "geburtstag": datetime.date.today().__str__()}
returnValue = collection.insert_one(insertList).inserted_id
