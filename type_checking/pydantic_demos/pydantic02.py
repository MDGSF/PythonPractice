# pydantic 可以自动将 JSON、字典等数据解析为 Python 对象。

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False


# 从字典解析
data = {"name": "Apple", "price": 1.99}
item = Item(**data)
print(item)


# JSON 数据
json_data = '{"name": "Banana", "price": 0.99}'
item = Item.model_validate_json(json_data)
print(item)
