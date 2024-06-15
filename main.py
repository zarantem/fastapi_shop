from fastapi import FastAPI
from config.settings import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from apps.brands.routers import app as brand_app
from apps.products.routers import app as category_app
from apps.categories.routers import app as product_app


app = FastAPI()


app.mount('/api/static', StaticFiles(directory='static'), name='static')

origin_cors = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin_cors,
    allow_methods=['*'],
    allow_headers=['*']
                   )


@app.on_event("startup")
async def startup():
    await engine.connect()


@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()



app.include_router(
    product_app
)


app.include_router(
    brand_app
)


app.include_router(
    category_app
)