from fastapi import Depends
from apps.base_repo.base_class import BaseService
from config.settings import get_session
from sqlalchemy.orm import Session
from .models import Brands


class BrandService(BaseService[Brands]):
    def __init__(self, db_session: Session):
        super(BrandService, self).__init__(Brands, db_session)


def get_brand_service(
    db_session: Session = Depends(get_session),
) -> BrandService:
    return BrandService(db_session)
