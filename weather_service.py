import requests

class WeatherService:
    def __init__(self, openweathermap_api_key, weatherapi_key):
        self.openweathermap_api_key = openweathermap_api_key
        self.weatherapi_key = weatherapi_key

    def get_openweathermap_data(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={{city}}&appid={{self.openweathermap_api_key}}'
        response = requests.get(url)
        return response.json()

    def get_weatherapi_data(self, city):
        url = f'https://api.weatherapi.com/v1/current.json?key={{self.weatherapi_key}}&q={{city}}'
        response = requests.get(url)
        return response.json()

    def get_weather(self, city):
        openweathermap_data = self.get_openweathermap_data(city)
        weatherapi_data = self.get_weatherapi_data(city)
        return {'openweathermap': openweathermap_data, 'weatherapi': weatherapi_data}