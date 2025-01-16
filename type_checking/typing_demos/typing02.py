from typing import List, Tuple

# 类型别名
Coordinates = Tuple[float, float]
Points = List[Coordinates]


def get_points() -> Points:
    return [(1.0, 2.0), (3.0, 4.0)]
