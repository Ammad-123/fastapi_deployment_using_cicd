from typing import Optional, Union 
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None  
class ItemResponse(ItemCreate):
    id: int