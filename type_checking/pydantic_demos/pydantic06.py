# pydantic 允许你为字段定义自定义验证逻辑，确保数据满足特定的业务规则。

from pydantic import BaseModel, field_validator


class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def check_age(cls, value):
        if value < 0:
            raise ValueError("Age must be a positive number")
        return value


try:
    user = User(name="John", age=-10)
except ValueError as e:
    print(e)
