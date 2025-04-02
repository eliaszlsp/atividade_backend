import oracledb
from dotenv import load_dotenv
import os

load_dotenv()


def conectar():
    try:
        conn = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )
        print("Conexão bem-sucedida!")
        return conn
    except oracledb.Error as e:
        print("Erro na conexão:", e)
        return None
