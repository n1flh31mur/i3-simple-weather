# i3-simple-weather
Python script for i3bar/polybar and other bars that supports python scripts.

This script make request to [OpenWeather](https://openweathermap.org/) and returns tempreture and [Font Awesome Pro](https://fontawesome.com/) icon that shows weather condition.

## Examples:
![Example 1](/screenshots/screenshot-1.png)
![Example 2](/screenshots/screenshot-2.png)
![Example 3](/screenshots/screenshot-3.png)

Icons that app shows, can be changed. For it, you need to open **weather.py** and change *values* in *key-value arrays*.

Also before script run, you have to set up script. Indicating your *api key*, *city*.
You can also change *units* and *temperature unit*.

## Settings example
```python
# Settings 
city = "Stockholm" # Your city 
api_key = "0a00a0000a0aa00a0a00aaa000000a00" # Your openweather api key
units = "metric" # Unit system {imperial or metric}
temperature_unit = "C" # Units of measurement. That will be showed in UI. Does not affect on API.
```

## Run script with polybar
```sh
[module/weather]
type = custom/script
interval = 600
cursor-click = python3 ~/.config/polybar/scripts/weather.py
exec = python3 ~/.config/polybar/scripts/weather.py
```
