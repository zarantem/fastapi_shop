from pydantic import BaseModel
from dataclasses import dataclass
from fastapi import UploadFile, File, Form
from apps.categories.schema import CategoryInfo
from apps.brands.schema import BrandInfo


@dataclass
class ProductCreateUpdate:
    name: str = Form(...)
    image: UploadFile = File(...)
    article: str = Form(...)
    price: float = Form(...)
    body: str = Form(...)
    category_id: int = Form(...)
    brand_id: int = Form(...)


class ProductInfo(BaseModel):
    id: int
    name: str
    price: float
    article: str
    image: str
    body: str
    category: CategoryInfo
    brand: BrandInfo


    class Config:
        orm_mode = True