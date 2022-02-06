import pyowm
import pyautogui
import math
import time
from config import api_key

lat, lon = 49.002124426630644, 12.100499639590657 # placeholder: coordinates in Regensburg

speed_factor = 1.0

def get_weather(weather_manager):
    weather_data = weather_manager.weather_at_coords(lat=lat, lon=lon) 

    wind = weather_data.weather.wind()
    wind_direction = wind['deg'] # in meteorological degrees: 0 is north, goes clockwise
    wind_speed = wind['speed'] # in meters/second

    print(f'direction: {wind_direction}, speed: {wind_speed}')
    return wind_direction, wind_speed

def update_cursor_speed(weather_manager):
    wind_direction, wind_speed = get_weather(weather_manager)

    # still pretty off
    x_vel = wind_speed * speed_factor * math.cos(math.radians(wind_direction))
    y_vel = wind_speed * speed_factor * math.sin(math.radians(wind_direction)) * -1
    return x_vel, y_vel

owm = pyowm.OWM(api_key)
print(dir(owm))
weather_manager = owm.weather_manager()

x_vel, y_vel = update_cursor_speed(weather_manager)
counter = 0

while True:
    pyautogui.moveRel(x_vel, y_vel)
    time.sleep(0.01)
    counter += 1
    if counter > 100:
        counter = 0
        x_vel, y_vel = update_cursor_speed(weather_manager)
