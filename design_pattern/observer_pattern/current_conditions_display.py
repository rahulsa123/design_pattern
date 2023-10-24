from design_pattern.observer_pattern.display_element import DisplayElement
from design_pattern.observer_pattern.observer import Observer
from design_pattern.observer_pattern.weather_data import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    temp:int
    humidity:float
    weather_data:WeatherData

    def __init__(self, weather_data:WeatherData) -> None:
        super().__init__()
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: int, humidity: float, pressure: float):
        self.temp = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions {self.temp=} degree and {self.humidity=}")