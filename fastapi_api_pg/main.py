from fastapi import FastAPI
import psycopg2
import os
import httpx

app = FastAPI(docs_url='/')

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)

    print("Database connected successfully")
except:
    print("Database not connected successfully")


@app.get("/{word}")
async def root(word: str):
    query = '''insert into student(name) values(%s);'''
    cur = conn.cursor()
    cur.execute(query, (word,))
    conn.commit()
    data = {
        'word': word
    }
    url = 'http://' + os.getenv('DJANGO_HOST') + ':' + os.getenv('DJANGO_PORT') + '/data'
    response = httpx.post(url, data=data)
    print(response.status_code)
    print(response)
    return {"message": "djangoga yuborildi"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event("startup")
async def on_startup():
    query = '''
    create table if not exists student(
        id serial primary key,
        name varchar(255)
    );
    '''
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
