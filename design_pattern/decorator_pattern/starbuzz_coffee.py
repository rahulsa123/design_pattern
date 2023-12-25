from design_pattern.decorator_pattern.beverage import Beverage
from design_pattern.decorator_pattern.dark_roast import DarkRoast
from design_pattern.decorator_pattern.espresso import Espresso
from design_pattern.decorator_pattern.mocha_decorator import MochaDecorator
from design_pattern.decorator_pattern.whip_decorator import WhipDecorator

if __name__ == '__main__':
    beverage: Beverage = Espresso()

    print(beverage.get_description(), " $", beverage.cost())

    beverage2:Beverage = DarkRoast()
    beverage2 = MochaDecorator(beverage2)
    beverage2 = MochaDecorator(beverage2)
    beverage2 = WhipDecorator(beverage2)

    print(beverage2.get_description(), " $", beverage2.cost())

