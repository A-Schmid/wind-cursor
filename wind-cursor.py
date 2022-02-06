import pyowm
from config import api_key

lat, lon = 49.002124426630644, 12.100499639590657 # placeholder: coordinates in Regensburg

owm = pyowm.OWM(api_key)
print(dir(owm))
weather_manager = owm.weather_manager()
weather_data = weather_manager.weather_at_coords(lat=lat, lon=lon) 

wind = weather_data.weather.wind()
wind_direction = wind['deg'] # in meteorological degrees: 0 is north, goes clockwise
wind_speed = wind['speed'] # in meters/second

print(f'direction: {wind_direction}, speed: {wind_speed}')
