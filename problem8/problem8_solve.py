from pymongo import MongoClient
from datetime import datetime

import pymongo
import pandas as pd
import random as rd

client = MongoClient()
db = client.haystax

# cursor =  db.documents.find().sort([
#     ("borough", pymongo.ASCENDING),
#     ("address.zipcode", pymongo.ASCENDING)
# ])

cursor = db.documents.aggregate([
    {
        "$unwind": "$words"
    },
    {
        "$sortByCount": "$words"
    }
])

for document in cursor:
    print(document)
