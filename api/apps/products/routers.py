from typing import Optional, List
from fastapi import APIRouter, Depends
from .sercvice import ProductService, get_product_service
from . import schema


app = APIRouter(prefix='/api/v1/categories', tags=['Продукт'])


@app.get('/', response_model=List[schema.ProductInfo], summary='Список')
async def list_id(limit: Optional[int] = 60, service: ProductService = Depends(get_product_service)):
    return await service.get_list(limit)


@app.get('/{id}', response_model=List[schema.ProductInfo], summary='Один item')
async def get_one_id(limit: int, service: ProductService = Depends(get_product_service)):
    return await service.get_one(id)


@app.post('/', status_code=201, summary='Создание')
async def create(data: schema.ProductCreateUpdate = Depends(),
                 service: ProductService = Depends(get_product_service)):
    return await service.create(data)


@app.delete('/{id}', summary='Удаление')
async def delete(id: int,
                 service: ProductService = Depends(get_product_service)):
    return await service.delete(id)