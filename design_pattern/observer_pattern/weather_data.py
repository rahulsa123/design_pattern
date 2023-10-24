from typing import List

from design_pattern.observer_pattern.observer import Observer
from design_pattern.observer_pattern.subject import Subject


class WeatherData(Subject):
    observers: List[Observer]
    temp: int
    humidity: float
    pressure: float

    def __init__(self) -> None:
        super().__init__()
        self.observers = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remover_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observer()

    def set_measurements(self, temp:int, humidity:float, pressure:float):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
