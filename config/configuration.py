import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

#Vamos a conectar con la base de datos de mongo en local
if not (DBURL):
    raise ValueError("You must specify a URL")


client = MongoClient(DBURL)
db = client.get_database()
collection = db["Sentiment"]
