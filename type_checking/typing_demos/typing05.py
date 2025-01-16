# Literal[value1, value2, ...]: 表示值必须是 value1, value2 等之一。

from typing import Literal


def set_status(status: Literal["active", "inactive"]) -> None:
    print(f"Status set to {status}")
