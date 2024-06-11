from api.config.settings import Base
from sqlalchemy import String, ForeignKey
from typing import Optional, List
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import relationship
from api.apps.brands.models import Brands
from api.apps.categories.models import Categories


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    article: Mapped[str]
    image: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'))
    category: Mapped['Categories'] = relationship(Categories, lazy="joined")
    brand: Mapped['Brands'] = relationship(Brands, lazy="joined")


    def __str__(self) -> str:
        return self.name