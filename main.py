from datetime import datetime
import edifice as ed
import pytz
import requests
from edifice import Label, TextInput, Button
from geopy import Nominatim
from timezonefinder import TimezoneFinder


class WeatherApp(ed.Component):

    @ed.register_props
    def __init__(self):
        super().__init__()
        self.humidity = 0
        self.pressure = 0
        self.feel_temperature = 0
        self.temperature = 0
        self.description = ""
        self.condition = ""
        self.current_time = ""
        self.city_new_name = "Mumbai"

    # def get_weather(self):
    #     city = self.city_new_name
    #     location = Nominatim(user_agent="geoapiExercises").geocode(city)
    #     obj = TimezoneFinder()
    #     result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    #     home = pytz.timezone(result)
    #     local_time = datetime.now(home)
    #     self.current_time = local_time.strftime("%I:%M %p")
    #     print(self.current_time)
    #     lat = str(location.latitude)
    #     lon = str(location.longitude)
    #     API_key = "ba7dd73aabf917793caee6fe1da2eb97"
    #     api = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + API_key
    #     print(api)
    #     json_data = requests.get(api).json()
    #     print(json_data)
    #     self.condition = json_data["weather"][0]["main"]
    #     self.description = json_data["weather"][0]["description"]
    #     self.temperature = int(int(json_data["main"]["temp"]) - 273.15)
    #     self.feel_temperature = int(int(json_data["main"]["feels_like"]) - 273.15)
    #     self.pressure = int(json_data["main"]["pressure"])
    #     self.humidity = int(json_data["main"]["humidity"])
    #     print("Values Assigned")

    def render(self):

        def get_weather():
            city = self.city_new_name
            location = Nominatim(user_agent="geoapiExercises").geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            self.current_time = local_time.strftime("%I:%M %p")
            print(self.current_time)
            lat = str(location.latitude)
            lon = str(location.longitude)
            API_key = "ba7dd73aabf917793caee6fe1da2eb97"
            api = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + API_key
            print(api)
            json_data = requests.get(api).json()
            print(json_data)
            self.set_state(condition=json_data["weather"][0]["main"])
            self.set_state(description = json_data["weather"][0]["description"])
            self.set_state(temperature = int(int(json_data["main"]["temp"]) - 273.15))
            self.set_state(feel_temperature = int(int(json_data["main"]["feels_like"]) - 273.15))
            self.set_state(pressure = int(json_data["main"]["pressure"]))
            self.set_state(humidity = int(json_data["main"]["humidity"]))
            print("Values Assigned")

        city_new_name = self.city_new_name
        city_name = city_new_name
        window_style = {"height": 500, "width": 900, "align": "justify", "background-color": "#46b8f9"}
        input_style_1 = {"width": 900, "height": 100, "align": "justify", "font-family": "serif"}
        input_style = {"width": 400, "height": 50, "background-color": "rgba(62,65,64,255)", "border-radius": 50,
                       "color": "white", "align": "center", "padding": 10, "font-size": 25, "font-weight": 500}
        search_style = {"width": 100, "height": 50, "background-color": "rgba(62,65,64,255)", "border-radius": 50,
                        "color": "white", "align": "center", "padding": 10, "font-size": 25, "font-weight": 500}
        heading_container = {"width": 900, "height": 75, "align": "justify"}
        heading_style = {"width": 900, "height": 75, "font-size": 30, "color": "black", "align": "center",
                         "font-weight": 700}
        temp_data_row_style = {"width": 900, "height": 50, "align": "justify"}
        temp_data_title_style = {"width": 450, "font-size": 20, "font-weight": 500, "align": "right"}
        temp_data_data_style = {"width": 450, "font-size": 20, "font-weight": 500, "align": "left"}
        return ed.View(layout="column", style=window_style)(
            ed.View(layout="row", style=input_style_1)(
                TextInput(city_name, style=input_style | {"margin-right": "2px solid #46b8f9"},
                          on_change=lambda text: self.set_state(city_new_name=text)),
                Button("Search", style=search_style, on_click=lambda e: get_weather()),
            ),
            ed.View(layout="row", style=heading_container)(
                Label("Current Temperature", style=heading_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label("Local Time : ", style=temp_data_title_style),
                Label(self.current_time, style=temp_data_data_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label("Temperature : ", style=temp_data_title_style),
                Label(f"{self.temperature}°C ", style=temp_data_data_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label(" Feels Like : ", style=temp_data_title_style),
                Label(f"{self.feel_temperature}°C ", style=temp_data_data_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label("Ambience : ", style=temp_data_title_style),
                Label(self.condition, style=temp_data_data_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label("Pressure : ", style=temp_data_title_style),
                Label(f"{self.pressure} hPa ", style=temp_data_data_style),
            ),
            ed.View(layout="row", style=temp_data_row_style)(
                Label("Humidity : ", style=temp_data_title_style),
                Label(f"{self.humidity} % ", style=temp_data_data_style),
            )
        )


ed.App(WeatherApp()).start()
