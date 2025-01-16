from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


# 可选字段可以省略
product = Product(name="Laptop", price=999.99)
print(product)
