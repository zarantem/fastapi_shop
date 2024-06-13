from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from api.apps.base_repo.base_class import BaseService
from api.config.settings import get_session
from .models import Brands


class BrandService(BaseService[Brands]):
    def __init__(self, db_session: AsyncSession):
        super(BrandService, self).__init__(Brands, db_session)


def get_brand_service(db_session:AsyncSession = Depends(get_session)) -> BrandService:
    return BrandService(db_session)