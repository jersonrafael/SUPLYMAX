import os
from dotenv import load_dotenv

from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongoUri = os.getenv('mongoUri')

# Create a new client and connect to the server
client = MongoClient(mongoUri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client[f'{os.getenv("db_name")}']
products = db[f'{os.getenv("first_collection")}']
categorys = db[f'{os.getenv("second_collection")}']