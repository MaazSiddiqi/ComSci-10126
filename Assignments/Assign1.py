# COMSCI 1026B – Assignment 1
# Maaz Siddiqi
# Calculate windchill / humidex based on a given temperature

import math


# Prompt user for input with {s}, check input validity, if invalid, output {invalid_out} for user feedback and retry
# NOTE: sample_name: type1 is syntax to ensure that parameter input for 'sample_name' is of type 'type1'
# NOTE: def sample_func() -> type2 is syntax to ensure that function returns value of type 'type2'
# NOTE: def sample_func(sample_name = sample_value) is syntax to assign default value to function if
# parameter input was omitted from function call
def prompt(s, values: list, invalid_out: str = 'That input is invalid.', range=False) -> str:
    # If values are range, ensure there is only a start and end, otherwise throw an error
    if range and len(values) != 2: raise Exception('Prompt range expects 2 values')

    # Take input and check validity in values, or if range is selected, check if within range
    # When input valid, return input
    # When input invalid, print {invalid_out} and retry
    while True:
        inp = input(s)
        if not range:
            for v in values:
                if inp == str(v):
                    return inp
        else:
            if float(values[0]) <= float(inp) < float(values[1]):
                return inp
        print(invalid_out)


# Calculates windchill based on temperature, {t}
def calc_windchill(t):
    wind_velocity = float(
        prompt('Enter a wind speed between 1 and 99 km/h: ', [1, 100], 'That wind speed is invalid.', range=True))

    # Calculate windchill from formula
    _wind_chill = round(13.12 + (0.6125 * t) - (11.37 * (wind_velocity ** 0.16)) + (0.3965 * t * (wind_velocity ** 0.16)))

    # Based on windchill, identify risk factor
    risk_factor = ''
    if _wind_chill <= DANGER_RISK_WC:
        risk_factor = 'Very High Risk. Skin can freeze in under 10 minutes.'
    elif _wind_chill <= HIGH_RISK_WC:
        risk_factor = 'High Risk. Skin can freeze in 10-30 minutes.'
    elif _wind_chill <= MEDIUM_RISK_WC:
        risk_factor = 'Moderate risk.'
    else:
        risk_factor = 'Low risk.'

    # Return a tuple (a, b) (brackets no necessary) for windchill and risk ; allows easy extraction of result to
    # variables after function call
    return _wind_chill, risk_factor


# Calculates humidex based on temperature, {t}
def calc_humidex(t):
    dew_point = float(
        prompt('Enter the dewpoint between -50 and 50: ', [-50, t + 1], 'That dew point is invalid.', range=True))

    # Calculate humidex from formula
    f = 6.11 * math.exp(5417.753 * (1 / 273.16 - 1 / (273.16 + dew_point)))
    g = 5 / 9 * (f - 10)
    _humidex = round(t + g)

    # Identify Risk Factor
    risk_factor = ''
    if _humidex >= DANGER_RISK_HUMIDEX:
        risk_factor = 'Dangerous. Heat stroke possible.'
    elif _humidex >= HIGH_RISK_HUMIDEX:
        risk_factor = 'Great discomfort. Avoid exertion.'
    elif _humidex >= MEDIUM_RISK_HUMIDEX:
        risk_factor = 'Some discomfort.'
    else:
        risk_factor = 'Little or no discomfort.'

    # Return a tuple (a, b) (brackets no necessary) for humidex and risk ; allows easy extraction of result to
    # variables after function call
    return _humidex, risk_factor


# Constants
WINDCHILL_START = 0
DANGER_RISK_WC = -40
HIGH_RISK_WC = -28
MEDIUM_RISK_WC = -10

HUMIDEX_START = 20
DANGER_RISK_HUMIDEX = 45
HIGH_RISK_HUMIDEX = 40
MEDIUM_RISK_HUMIDEX = 30


# Main Program,
# 'while True' will force the loop to always loop unless forcefully broken out of using a 'break' statement
while True:
    # Get temperature from user
    temp = float(prompt('Enter a temperature between -50 and 50: ', [-50, 50],
                        'That temperature is invalid.', range=True))

    # Based on temp, find windchill or humidex
    if temp <= WINDCHILL_START:
        # windchill
        print('Calculating windchill.')
        wind_chill, risk = calc_windchill(temp)             # Function returns a tuple (a, b), which you can extract
        print(f'The windchill is {wind_chill}. {risk}')     # using a, b = (a, b)
    elif temp >= HUMIDEX_START:
        # humidex
        print('Calculating humidex.')
        humidex, risk = calc_humidex(temp)                  # Function returns a tuple (a, b), which you can extract
        print(f'The humidex is {humidex}. {risk}')          # using a, b = (a, b)
    else:
        # Neither
        print('Windchill and humidex are not a factor at this temperature.')

    # Prompt user to try again, if no, exit loop
    res = prompt('Check another weather condition (Y/N)? ', ['Y', 'N', 'y', 'n'])
    if res.lower() == 'n':
        # Force out of the program loop using python 'break' statement which terminates the loop it is inside of
        break
# Program End
