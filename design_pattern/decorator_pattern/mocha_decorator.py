from design_pattern.decorator_pattern.beverage import Beverage
from design_pattern.decorator_pattern.condiment import CondimentDecorator


class MochaDecorator(CondimentDecorator):
    def __init__(self, beverage:Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + .20
