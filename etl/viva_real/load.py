import json
import sys
sys.path.append("../")
from src.database import Database

with open('transformed.json', 'r') as f:
    data = json.load(f)

db = Database()
inserted = db.bulk_create('viva_real', data)

print(inserted)