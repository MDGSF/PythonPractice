from typing import int, float, str, bool, bytes
from typing import List, Dict, Set, Tuple
from typing import Optional
from typing import Union
from typing import Any


def greet(name: str) -> str:
    return f"Hello, {name}"


def process_data(data: List[int]) -> Dict[str, int]:
    return {"length": len(data)}


def get_coordinates() -> Tuple[float, float]:
    return (3.14, 2.71)


# Optional[str] 和 str | None 在功能上是完全等价的
# Optional[T] 是 Union[T, None] 的简写形式
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "John Doe"
    return None


def parse_value(value: Union[int, str]) -> float:
    if isinstance(value, int):
        return float(value)
    return float(value)


def log_value(value: Any) -> None:
    print(f"Value: {value}")
