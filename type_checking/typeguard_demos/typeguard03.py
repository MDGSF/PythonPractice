from typeguard import typechecked
from typing import Generator


@typechecked
def generate_numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


# 正确调用
for num in generate_numbers(3):
    print(num)

# 错误调用（类型不匹配）
for num in generate_numbers("3"):  # 抛出 TypeError
    print(num)
