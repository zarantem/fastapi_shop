from fastapi import FastAPI
from config.settings import settings


app = FastAPI()


@app.get('/')
def test():
    return {'db_name':settings.db_url}