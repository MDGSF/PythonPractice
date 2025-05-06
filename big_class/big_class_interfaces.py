from typing import Protocol, runtime_checkable
from big_class_context import BigClassContext


@runtime_checkable
class IBigClass(Protocol):
    ctx: BigClassContext

    def get_shared_value(self, key: str) -> int: ...

    def update_shared_value(self, key: str, value: int) -> None: ...
