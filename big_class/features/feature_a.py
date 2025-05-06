from big_class_interfaces import IBigClass


class FeatureA:
    def __init__(self, big_class: IBigClass):
        self.big_class = big_class

    def process_data(self) -> int:
        value = self.big_class.get_shared_value("count")
        self.big_class.update_shared_value("count", value + 1)
        return value

    def show_context(self):
        print(f"name: {self.big_class.ctx.name}")
        print(f"age: {self.big_class.ctx.age}")
