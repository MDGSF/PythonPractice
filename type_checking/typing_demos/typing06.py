# Iterable[T]: 可迭代对象，元素类型为 T。
# Sequence[T]: 序列类型（如列表、元组），元素类型为 T。
# Mapping[K, V]: 映射类型（如字典），键类型为 K，值类型为 V。
# Type[T]: 表示类型 T 本身（用于注解类或类型）。
# NoReturn: 表示函数没有返回值（即函数总是抛出异常或无限循环）。

from typing import Iterable, Sequence, Mapping, Type, NoReturn


def process_items(items: Iterable[int]) -> None:
    for item in items:
        print(item)


def raise_error() -> NoReturn:
    raise ValueError("An error occurred")
