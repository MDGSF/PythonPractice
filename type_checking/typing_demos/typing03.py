# TypeVar: 用于定义泛型类型变量。
# Generic: 用于定义泛型类。

from typing import TypeVar, Generic, List

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content


def first_item(items: List[T]) -> T:
    return items[0]
