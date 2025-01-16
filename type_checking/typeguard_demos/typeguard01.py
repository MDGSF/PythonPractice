from typeguard import typechecked


@typechecked
def greet(name: str) -> str:
    return f"Hello, {name}"


# 正确调用
print(greet("Alice"))  # 输出: Hello, Alice

# 错误调用（类型不匹配）
print(greet(42))  # 抛出 TypeError
