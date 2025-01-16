# pydantic 可以轻松地将模型实例转换为字典或 JSON 格式

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


item = Item(name="Apple", price=1.99)
print(item.model_dump())  # 转换为字典
print(item.model_dump_json())  # 转换为 JSON
