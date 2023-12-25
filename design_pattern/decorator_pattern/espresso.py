from design_pattern.decorator_pattern.beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        super(Espresso, self).__init__(description="Espresso")

    def cost(self) -> float:
        return 1.99
