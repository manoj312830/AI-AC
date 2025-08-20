def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15

def fahrenheit_to_kelvin(f):
    """Convert Fahrenheit to Kelvin."""
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    """Convert Kelvin to Fahrenheit."""
    return (k - 273.15) * 9/5 + 32

def get_temperature_input(scale):
    """Prompt user to enter temperature in the given scale."""
    while True:
        try:
            value = float(input(f"Enter temperature in {scale}: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def display_menu():
    print("\n--- Temperature Converter ---")
    print("Select the conversion you want to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        if choice == '1':
            c = get_temperature_input("Celsius")
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C = {f:.2f}°F")
        elif choice == '2':
            f = get_temperature_input("Fahrenheit")
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F = {c:.2f}°C")
        elif choice == '3':
            c = get_temperature_input("Celsius")
            k = celsius_to_kelvin(c)
            print(f"{c}°C = {k:.2f}K")
        elif choice == '4':
            k = get_temperature_input("Kelvin")
            c = kelvin_to_celsius(k)
            print(f"{k}K = {c:.2f}°C")
        elif choice == '5':
            f = get_temperature_input("Fahrenheit")
            k = fahrenheit_to_kelvin(f)
            print(f"{f}°F = {k:.2f}K")
        elif choice == '6':
            k = get_temperature_input("Kelvin")
            f = kelvin_to_fahrenheit(k)
            print(f"{k}K = {f:.2f}°F")
        elif choice == '7':
            print("Exiting the Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
