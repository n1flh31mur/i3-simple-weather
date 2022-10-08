#    i3-simple-weather  Copyright (C) 2022  BrutalWizard (https://github.com/bru74lw1z4rd).
#    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions;

# More info about wether at - https://openweathermap.org/weather-conditions
# To show icons from this script you will need to buy "Font Awesome Pro" font - https://fontawesome.com/
# Also you can change icon in arrays to yours icons

import requests
import json

# Settings 
city = "" # Your town 
api_key = "" # Your openweather api key
units = "metric" # Unit system {imperial or metric}
temperature_unit = "C" # Units of measurement. That will be showed in UI. Does not affect on API.


def main():
    try:
        # Get data from openweather
        url = ('http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}').format(city, units, api_key)
        result = requests.get(url)

        # If result was received
        if(result.status_code == requests.codes['ok']):        
                # Read json
                weather = result.json()

                # Get info from array 
                id = int(weather['weather'][0]['id'])
                group = weather['weather'][0]['main'].capitalize()
                temp = int(float(weather['main']['temp']))

                # Load another icons for Atmosphere group
                if(group == "Atmosphere"):
                    return '{}°{}'.format(temp, temperature_unit)

                return '{}°{}'.format(temp, temperature_unit)
        else:
            return "" # Return reload icon
    except:
        return "" # Return reload icon

if __name__ == "__main__":
	print(main())
