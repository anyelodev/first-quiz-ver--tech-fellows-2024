################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

# Creamos el diccionario para almacenar información de temperatura de ciudades
city_temperatures = {
    "Quito": 22,
    "Sao Paulo": 17,
    "San Francisco": 16
}

# Creamos el diccionario para almacenar información de condiciones climáticas de las ciudades
city_weather_conditions = {
    "Quito": "soleado",
    "Sao Paulo": "nublado",
    "San Francisco": "lluvioso"
}

def get_city_temperature(city):
    # Obtener la temperatura de la ciudad o devolver None si la ciudad no se encuentra en el diccionario
    return city_temperatures.get(city, None)

def get_city_weather(city):
    # Obtener la condición climática de la ciudad o devolver None si la ciudad no se encuentra en el diccionario
    sky_condition = city_weather_conditions.get(city, None)

    temperature = get_city_temperature(city)

    if temperature is not None and sky_condition is not None:
        return sky_condition
    else:
        return "'Ciudad no encontrada'"  # Devuelve un mensaje de "Ciudad no encontrada" para las cuidades que no se encuentran en los diccionarios

city_name = "Sao Paulo"

temperature = get_city_temperature("Quito")
weather = get_city_weather("Quito")

# Imprime los resultados
if temperature is not None and weather is not None:
    print(f"La temperatura en {city_name}, es de {temperature} grados y {weather}.")
else:
    print(f"No se pudo encontrar información para la ciudad {city_name}.")


