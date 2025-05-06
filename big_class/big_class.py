from features.feature_a import FeatureA
from features.feature_b import FeatureB
from big_class_interfaces import IBigClass
from big_class_context import BigClassContext


class BigClass(IBigClass):
    def __init__(self):
        self.ctx = BigClassContext()
        self.ctx.shared_state = {"count": 0}
        feature_a = FeatureA(self)
        self.feature_a = feature_a
        self.feature_b = FeatureB(self, feature_a)

    def get_shared_value(self, key: str) -> int:
        return self.ctx.shared_state[key]

    def update_shared_value(self, key: str, value: int) -> None:
        self.ctx.shared_state[key] = value

    def call_feature_a_show(self):
        self.feature_a.show_context()
