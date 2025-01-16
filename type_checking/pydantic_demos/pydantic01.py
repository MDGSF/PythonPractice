# 当数据传入模型时，pydantic 会自动验证数据是否符合定义的类型和规则

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str
    email: str


# 正确数据
user = User(id=1, name="John Doe", email="john.doe@example.com")
print(user)

# 错误数据
try:
    user = User(id="not_an_int", name="John Doe", email="john.doe@example.com")
except ValidationError as e:
    print(e)
