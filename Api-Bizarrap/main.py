from fastapi import FastAPI
import psycopg2

app = FastAPI(title="Bizarrap")

connection = psycopg2.connect(
    dbname="bizaList",
    user="postgres",
    password="12345",
    host="localhost"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM music")
results = cursor.fetchall()
cursor.close()

@app.get("/music")
async def get_music():
    return results