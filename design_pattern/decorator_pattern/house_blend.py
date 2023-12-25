from design_pattern.decorator_pattern.beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        super(HouseBlend, self).__init__(description="House Blend Coffee")

    def cost(self) -> float:
        return .89
