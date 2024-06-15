from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from apps.base_repo.base_class import BaseService
from config.settings import get_session
from .models import Categories


class CategoryService(BaseService[Categories]):
    def __init__(self, db_session: AsyncSession):
        super(CategoryService, self).__init__(Categories, db_session)


def get_category_service(db_session:AsyncSession = Depends(get_session)) -> CategoryService:
    return CategoryService(db_session)