
def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()
    if from_unit == to_unit:
        return value
    # Convert from from_unit to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit")
    # Now convert from Celsius to to_unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit")

print("Units: C for Celsius, F for Fahrenheit, K for Kelvin")
temp_value = float(input("Enter the temperature value: "))
current_unit = input("Enter the current unit (C/F/K): ")
convert_unit = input("Enter the unit to convert to (C/F/K): ")

try:
    result = convert_temperature(temp_value, current_unit, convert_unit)
    print(f"{temp_value:.2f} {current_unit.upper()} is {result:.2f} {convert_unit.upper()}")
except ValueError as e:
    print(e)

