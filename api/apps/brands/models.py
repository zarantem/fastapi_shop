from api.config.settings import Base
from sqlalchemy import String
from typing import Optional, List
from sqlalchemy.orm import mapped_column, Mapped
from api.apps.products.models import Products
from api.apps.categories.models import Categories


class Brands(Base):
    __tablename__='brands'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    slug:Mapped[str] = mapped_column(unique=True)

    def __str__(self) -> str:
        return self.name