import abc
from abc import ABC

from design_pattern.decorator_pattern.beverage import Beverage


class CondimentDecorator(Beverage, ABC):
    beverage: Beverage = None

    def __init__(self, description:str=""):
        super(CondimentDecorator, self).__init__(description=description)
