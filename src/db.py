import os
from pymongo import MongoClient
from datetime import datetime

client = MongoClient(os.getenv("MONGO_URI"))
db = client["soccer_llm"]

def get_player(name):
    return db.players.find_one({"name": name})

def save_summary(name, summary):
    db.requests.insert_one({
        "player_name": name,
        "summary": summary,
        "timestamp": datetime.utcnow()
    })
