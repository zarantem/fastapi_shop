from pydantic import BaseModel
from typing import Optional


class CategoryCreateUpdate(BaseModel):
    id: Optional[int] = None
    name: str
    slug: str

    class Config:
        from_attributes = True


class CategoryInfo(CategoryCreateUpdate):
    id: int