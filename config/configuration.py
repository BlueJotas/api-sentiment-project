import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

# Here, we will connect to our local mongo database:
if not (DBURL):
    raise ValueError("You must specify a URL")

# This gets the collection inside our database that we will work with!
client = MongoClient(DBURL)
db = client.get_database()
collection = db["Sentiment"]
