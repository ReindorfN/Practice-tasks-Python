"""
Take input of the air temperature and wind speed and then compute the wind  chill index rounded to the closest integer.
"""

air_temperature = int(input("Input air temperature: "))
wind_speed = int(input("Input wind speed: "))

wind_chill_index = 13.12 + (0.6215 * air_temperature) - (11.37 * wind_speed **0.16) + (0.3965*air_temperature*(wind_speed**0.16))
wind_chill_index = round(wind_chill_index)
print("The Wind Chill Index is", wind_chill_index, "degrees Celsius.")