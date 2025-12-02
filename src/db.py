from pymongo import MongoClient
import os
from datetime import datetime

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("MONGO_DB", "soccer_llm")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
summaries = db["summaries"]


def normalize_name(name: str) -> str:
    return name.lower().replace(" ", "_")


def get_cached_summary(player_name: str):
    """Return the cached record if exists."""
    key = normalize_name(player_name)
    return summaries.find_one({"_id": key})


def store_summary(player_name: str, facts: str, summary_json: dict):
    """Insert or replace summary in MongoDB."""
    key = normalize_name(player_name)
    doc = {
        "_id": key,
        "player_name": player_name,
        "facts": facts,
        "summary": summary_json,
        "timestamp": datetime.utcnow().isoformat()
    }
    summaries.replace_one({"_id": key}, doc, upsert=True)
    return doc
