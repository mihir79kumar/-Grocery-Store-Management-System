import os
import mysql.connector
from dotenv import load_dotenv

# Load database configuration from .env file
load_dotenv()

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    db_user = os.getenv('DB_USER', 'root')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_DATABASE', 'grocery_store')
    
    __cnx = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

  return __cnx

