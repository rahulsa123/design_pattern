from design_pattern.decorator_pattern.beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        super(DarkRoast, self).__init__(description="Dark Roast")

    def cost(self) -> float:
        return 0.99
