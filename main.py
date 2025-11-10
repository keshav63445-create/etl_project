import mariadb
import sys
from dotenv import load_dotenv

load_dotenv()

# 1. Database Connection Parameters
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'user_name',
    'password': 'password',
    'database': 'your_database_name'
}

conn = mariadb