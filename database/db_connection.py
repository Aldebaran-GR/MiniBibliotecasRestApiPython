import os
import psycopg2
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()
 
# Obtener variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Conectar a PostgreSQL
def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
            )
        print("✅ Conexión exitosa a PostgreSQL")
        return connection
    except Exception as e:
        print("❌ Error al conectar a la base de datos:", e)
        return None