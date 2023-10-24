from design_pattern.observer_pattern.current_conditions_display import CurrentConditionsDisplay
from design_pattern.observer_pattern.heat_index_display import HeatIndexDisplay
from design_pattern.observer_pattern.weather_data import WeatherData

if __name__ =="__main__":
    print("Data")
    weather_data = WeatherData()
    current_condition_display:CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)
    heat_index_display: HeatIndexDisplay = HeatIndexDisplay(weather_data)
    weather_data.set_measurements(20, 50.6, 30.5)
    weather_data.set_measurements(30, 60.6, 40.5)
    weather_data.set_measurements(40, 90.6, 50.5)

    # reason behind adding CurrentConditionsDisplay as observer into WeatherData
    weather_data.remover_observer(current_condition_display)
    weather_data.set_measurements(10, 10.6, 10.5)
    weather_data.set_measurements(10, 10.6, 20.5)

    weather_data.register_observer(current_condition_display)
    weather_data.set_measurements(20, 20.6, 20.5)
    weather_data.set_measurements(20, 20.6, 20.5)
