from pymongo import MongoClient
from datetime import datetime

import pymongo
import pandas as pd
import random as rd

client = MongoClient()
db = client.haystax

db.documents.remove()

words_db = pd.read_csv("../20k.txt", sep=" ", header=None)
words_db = words_db.sample(frac=0.1, replace=True)
print(words_db.size)
# sample = words_db.sample(3);
# for word in sample[0]:
#     print(word)
#
# print("--------------")
# print(sample[0].tolist())

rd.seed(123456789)
for i in range(100):
    sample = words_db.sample(rd.randint(90,140));
    words = sample[0].tolist()
    date_str = "2018-01-"
    date_str += str(rd.randint(1, 10))
    db.documents.insert_one(
    {
        "words": words,
        "date": datetime.strptime(date_str, "%Y-%m-%d")
    }
    )
