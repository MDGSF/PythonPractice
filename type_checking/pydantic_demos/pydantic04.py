# pydantic 支持复杂的数据类型，如嵌套模型、列表、字典、枚举等

from typing import List
from pydantic import BaseModel


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    addresses: List[Address]


user = User(
    name="John Doe",
    addresses=[
        {"city": "New York", "country": "USA"},
        {"city": "London", "country": "UK"},
    ],
)
print(user)
