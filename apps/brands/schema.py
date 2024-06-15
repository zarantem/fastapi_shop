from pydantic import BaseModel
from typing import Optional


class BrandCreateUpdate(BaseModel):
    id: Optional[int] = None
    name: str
    slug: str


    class Config:
        from_attributes = True


class BrandInfo(BrandCreateUpdate):
    id: int