from typing import Optional, List
from fastapi import APIRouter, Depends
from .sercvice import BrandService, get_brand_service
from . import schema


app = APIRouter(prefix='/api/v1/brands', tags=['Бренд'])


@app.get('/', response_model=List[schema.BrandInfo], summary='Список')
async def list_id(limit: Optional[int] = 60, service: BrandService = Depends(get_brand_service)):
    return await service.get_list(limit)


@app.get('/{id}', response_model=List[schema.BrandInfo], summary='Один item')
async def get_one_id(limit: int, service: BrandService = Depends(get_brand_service)):
    return await service.get_one(id)


@app.post('/', summary='Создание', status_code=201)
async def create(data: schema.BrandCreateUpdate,
                 service: BrandService = Depends(get_brand_service)):
    return await service.create(data)


@app.delete('/{id}', summary='Удаление')
async def delete(id: int,
                 service: BrandService = Depends(get_brand_service)):
    return await service.delete(id)