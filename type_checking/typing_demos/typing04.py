# Callable[[Arg1Type, Arg2Type, ...], ReturnType]: 表示一个可调用对象（如函数），参数类型为 Arg1Type, Arg2Type，返回类型为 ReturnType

from typing import Callable


def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
