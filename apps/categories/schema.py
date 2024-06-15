from pydantic import BaseModel
from typing import Optional


class CategoryCreateUpdate(BaseModel):
    id: Optional[int] = None
    name: str
    slug: str

    class Config:
        orm_mode = True


class CategoryInfo(CategoryCreateUpdate):
    id: int