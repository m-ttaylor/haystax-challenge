from pymongo import MongoClient
from datetime import datetime

import pymongo
import pandas as pd
import random as rd

client = MongoClient()
db = client.haystax

cursor1 = db.documents.aggregate([
    {
        "$unwind": "$words"
    },
    {
        "$sortByCount": "$words"
    }
])

# temp = db.documents.find({'date':datetime.strptime("2018-01-08", "%Y-%m-%d")})
cursor2 = db.documents.aggregate([
	{
		"$match": 
		{
				'date':datetime.strptime("2018-01-08", "%Y-%m-%d")
		}
	},
	{
        "$unwind": "$words"
    },
    {
        "$sortByCount": "$words"
    }
])

# need to use count because the cursors are iterators
count = 0
for document in cursor1:
	count +=1
	if count <= 1:
		print("most frequent word is '{}', with {} occurences".format(document['_id'], document['count']))

count = 0
for document in cursor2:
	count +=1
	if count <= 1:
		print("most frequent word in past day is '{}', with {} occurences".format(document['_id'], document['count']))