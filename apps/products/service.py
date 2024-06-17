from fastapi import Depends
from apps.base_repo.base_class import BaseService
from config.settings import get_session
from .models import Products
import os
from utils.save_image import image_add_origin
from sqlalchemy.orm import Session


class ProductService(BaseService[Products]):
    def __init__(self, db_session: Session):
        super(ProductService, self).__init__(Products, db_session)

    async def create(self, product):
        path_folder = "api/static/images/products"
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)
        path_image = image_add_origin(
            product.image, "api/static/images/products"
        )
        async with self.db_session as session:
            new_product = self.table(
                name=product.name,
                image=path_image,
                article=product.article,
                price=product.price,
                body=product.body,
                category_id=product.caegory_id,
                brand_id=product.brand_id,
            )
            session.add(new_product)
            await session.commit()
        return new_product


def get_product_service(
    db_session: Session = Depends(get_session),
) -> ProductService:
    return ProductService(db_session)
