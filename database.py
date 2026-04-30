import os
from dotenv import load_dotenv

load_dotenv()
DB_PASSWORD = os.getenv("DB_PASSWORD")
API_KEY_AMAZON = os.getenv("API_KEY_AMAZON")

def connect_db():
    print (f"Connnessione in corso {DB_PASSWORD}")
    print (f"Connnessione in corso {API_KEY_AMAZON}")