from fastapi import Depends
from apps.base_repo.base_class import BaseService
from config.settings import get_session
from sqlalchemy.orm import Session
from .models import Categories


class CategoryService(BaseService[Categories]):
    def __init__(self, db_session: Session):
        super(CategoryService, self).__init__(Categories, db_session)


def get_category_service(
    db_session: Session = Depends(get_session),
) -> CategoryService:
    return CategoryService(db_session)
