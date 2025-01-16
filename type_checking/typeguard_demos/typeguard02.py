from typeguard import typechecked


class Person:
    @typechecked
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @typechecked
    def celebrate_birthday(self) -> None:
        self.age += 1


# 正确调用
person = Person("Alice", 30)
person.celebrate_birthday()

# 错误调用（类型不匹配）
person = Person("Bob", "30")  # 抛出 TypeError
