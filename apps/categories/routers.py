from typing import Optional, List
from fastapi import APIRouter, Depends
from .sercvice import CategoryService, get_category_service
from . import schema


app = APIRouter(prefix='/api/v1/categories', tags=['Категория'])


@app.get('/', response_model=List[schema.CategoryInfo], summary='Список')
async def list_id(limit: Optional[int] = 60, service: CategoryService = Depends(get_category_service)):
    return await service.get_list(limit)


@app.get('/{id}', response_model=List[schema.CategoryInfo], summary='Один item')
async def get_one_id(limit: int, service: CategoryService = Depends(get_category_service)):
    return await service.get_one(id)


@app.post('/', summary='Создание', status_code=201)
async def create(data: schema.CategoryCreateUpdate,
                 service: CategoryService = Depends(get_category_service)):
    return await service.create(data)


@app.delete('/{id}', summary='Удаление')
async def delete(id: int,
                 service: CategoryService = Depends(get_category_service)):
    return await service.delete(id)