from big_class_interfaces import IBigClass
from .feature_a import FeatureA


class FeatureB:
    def __init__(self, big_class: IBigClass, a: FeatureA):
        self.big_class = big_class
        self.a = a

    def process_data(self) -> int:
        value = self.big_class.get_shared_value("count")
        self.big_class.update_shared_value("count", value + 1)
        return value

    def show(self):
        self.a.show_context()
