# wind-cursor

Use a real time weather API to apply wind to your mouse cursor.

## Requirements

 * [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
 * [pyowm](https://pyowm.readthedocs.io)

## Usage

This program uses the [OpenWeatherMap](https://home.openweathermap.org/) API.
Therefore, you have to register and get your own API key to use this program.
Sucks like hell - I mean, why not just make friggin **Weather Data** publicly accessible?

Anyhow - install the [pyowm](https://pyowm.readthedocs.io) package, register at OWM's website, get your API key.
Then, create a `config.py` file and add the line `api_key = 'YOUR_KEY_HERE'`.
