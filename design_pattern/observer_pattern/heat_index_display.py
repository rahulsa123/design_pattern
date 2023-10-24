from design_pattern.observer_pattern.display_element import DisplayElement
from design_pattern.observer_pattern.observer import Observer
from design_pattern.observer_pattern.weather_data import WeatherData


class HeatIndexDisplay(Observer, DisplayElement):
    heat_index: float
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: int, humidity: float, pressure: float):
        self.compute_heat_index(temp, humidity)
        self.display()

    def display(self):
        print(f"Heat index :{self.heat_index}")

    def compute_heat_index(self, t, rh):
        self.heat_index = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
                            + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh))
                            + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                            (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                                                                                                (rh * rh * rh)) + (
                                        0.00000142721 * (t * t * t * rh)) +
                            (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                            0.000000000843296 * (t * t * rh * rh * rh)) -
                           (0.0000000000481975 * (t * t * t * rh * rh * rh)))
