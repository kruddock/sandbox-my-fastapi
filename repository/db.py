from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('DB_CONNECTION', '')
client = MongoClient(uri)

database = client.get_database("sandbox")
