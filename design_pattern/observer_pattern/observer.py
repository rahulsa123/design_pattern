import abc


class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, temp: int, humidity: float, pressure: float):
        pass
