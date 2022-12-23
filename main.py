from datetime import datetime
import edifice as ed
import pytz
import requests
from edifice import Label, TextInput, Button, Image
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
        self.max_temp = 0
        self.visibility = 0
        self.wind = 0
        self.description = ""
        self.condition = ""
        self.current_time = ""
        self.city_new_name = ""

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
            json_data = requests.get(api).json()
            self.set_state(condition=json_data["weather"][0]["main"])
            self.set_state(description = json_data["weather"][0]["description"])
            self.set_state(temperature = int(int(json_data["main"]["temp"]) - 273.15))
            self.set_state(feel_temperature = int(int(json_data["main"]["feels_like"]) - 273.15))
            self.set_state(pressure = int(json_data["main"]["pressure"]))
            self.set_state(humidity = int(json_data["main"]["humidity"]))
            self.set_state(visibility = int(json_data["visibility"]))
            self.set_state(wind = int(json_data["wind"]["speed"]))
            self.set_state(max_temp = int(int(json_data["main"]["temp_max"])-273.15))

        city_new_name = self.city_new_name
        city_name = city_new_name
        window_style = {"width": 900, "height": 500, "align": "justify", "background-color": "#041c3c"}
        title_bar = {"width": 900, "height": 100, "align": "justify"}
        title_style = {"width": 300, "font-size": 30, "padding": 10, "font-weight": 700, "color": "white"}
        city_search_container = {"align": "justify", "border-radius": 20, "background-color": "white"}
        search_text = {"width": 400, "height": 50, "background-color": "transparent", "border-radius": 50,
                       "color": "black", "align": "center", "padding": 10, "font-size": 25, "font-weight": 500}
        search_style = {"width": 100, "height": 50, "background-color": "transparent", "border-radius": 50,
                        "color": "black", "align": "center", "padding": 10, "font-size": 25, "font-weight": 500}
        heading_style = {"max-width": 900, "height": 35, "font-size": 25, "color": "#cdcdcd", "align": "left",
                         "font-weight": 700, "padding": 10}
        time_display = {"width": 200, "font-size": 35, "font-weight": 500, "align": "left", "padding": 10, "color": "white"}
        temp_display = {"width": 200, "height": 75, "font-size": 70, "color": "white", "align": "justify",
                         "font-weight": 700, "padding": 10}
        feel_temp_display = {"width": 200, "height": 25, "font-size": 25, "color": "#cdcdcd", "align": "left",
                        "font-weight": 500, "padding": 10}
        disp_style = {"max-width": 900, "font-size": 25, "color": "white", "align": "left", "font-weight": 600, "padding": 10}
        return ed.View(layout="column", style=window_style)(
            ed.View(layout="row", style=title_bar)(
                Label("API Weather", style=title_style),
                ed.View(layout="row", style={"margin": 20})(
                    ed.View(layout="row", style=city_search_container)(
                        TextInput(city_name, style=search_text, on_change=lambda text: self.set_state(city_new_name=text)),
                        Button("Search", style=search_style, on_click=lambda e: get_weather())
                    )
                ),
            ),
            ed.View(layout="row", style={"height": 250, "width": 900})(
                ed.View(layout="column", style={"align": "top"})(
                    Label("Current Temp", style=heading_style),
                    Label(self.current_time, style=time_display)
                ),
                Image(src="weather.png",scale_to_fit=True, style={"height": 250, "width": 250}),
                ed.View(layout="column", style={"align":"justify"})(
                    Label(f"{self.temperature}°C ", style=temp_display),
                    Label(f"feels like: {self.feel_temperature}°C ", style=feel_temp_display)
                ),
            ),
            ed.View(layout="row", style={"height": 150, "width": 900, "padding":10})(
                ed.View(layout="column", style={"height": 130, "width": 430, "padding": 10, "align":"left"})(
                    ed.View(layout="row", style={"width": 430,"align":"left"})(
                        Label("Pressure: ", style=heading_style),
                        Label(f"{self.pressure} hPa ", style=disp_style),
                    ),
                    ed.View(layout="row", style={"width": 430, "align": "left"})(
                        Label("Humidity: ", style=heading_style),
                        Label(f"{self.humidity} % ", style=disp_style),
                    ),
                    ed.View(layout="row", style={"width": 430, "align": "left"})(
                        Label("MaxTemp: ", style=heading_style),
                        Label(f"{self.max_temp}°C ", style=disp_style),
                    ),
                ),
                ed.View(layout="column")(
                    ed.View(layout="row", style={"width": 430, "align": "left"})(
                        Label("Condition: ", style=heading_style),
                        Label(f"{self.condition}, {self.description}", style=disp_style),
                    ),
                    ed.View(layout="row", style={"width": 430, "align": "left"})(
                        Label("Visibility: ", style=heading_style),
                        Label(f"{self.visibility}m ", style=disp_style),
                    ),
                    ed.View(layout="row", style={"width": 430, "align": "left"})(
                        Label("Wind Speed: ", style=heading_style),
                        Label(f"{self.wind} m/s ", style=disp_style),
                    ),
                )
            ),
        )


ed.App(WeatherApp()).start()
