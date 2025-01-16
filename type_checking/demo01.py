# pip install -i https://mirrors.aliyun.com/pypi/simple/ mypy
# pip install -i https://mirrors.aliyun.com/pypi/simple/ monkeytype
# pip install -i https://mirrors.aliyun.com/pypi/simple/ pytype
# pip install -i https://mirrors.aliyun.com/pypi/simple/ typeguard

from typing import List, Dict
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


def process_data(data: List[int]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for idx, value in enumerate(data):
        result[f"item_{idx}"] = value
    return result
