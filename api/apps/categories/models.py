from api.config.settings import Base
from sqlalchemy import String, ForeignKey
from typing import Optional, List
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship
from api.apps.brands.models import Brands
from api.apps.products.models import Products


class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price:Mapped[float]
    article:Mapped[str]
    image:Mapped[str]
    category_id:Mapped[int] = mapped_column(ForeignKey('categories.id'))
    brand_id:Mapped[int] = mapped_column(ForeignKey('brands.id'))
    category:Mapped['Categories'] = relationship()
    brand:Mapped['Brands'] = relationship()



    def __str__(self) -> str:
        return self.name