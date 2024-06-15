from config.settings import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
#from sqlalchemy.orm import relationship
#from apps.products.models import Products as product_model
#from apps.brands.models import Brands as brand_model


class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    article: Mapped[str]
    image: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'))
    #product: Mapped['Products'] = relationship(product_model, lazy='joined')
    #brand: Mapped['Brands'] = relationship(brand_model, lazy='joined')



    def __str__(self) -> str:
        return self.name