import abc


class Beverage(abc.ABC):

    def __init__(self, description: str = "Unknown Beverage"):
        self.description = description

    def get_description(self) -> str:
        return self.description

    @abc.abstractmethod
    def cost(self) -> float:
        raise NotImplementedError
