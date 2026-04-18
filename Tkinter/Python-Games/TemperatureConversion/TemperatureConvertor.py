def convert_from_celcius_to_kelvin(cel):
    return cel + 273.15

def convert_from_kelvin_to_celcius(kel):
    return kel -273.15

def convert_from_fahrenheit_to_celsius(fah):
    return (fah - 32)*5/9

def convert_from_celsius_to_fahrenheit(cel):
    return cel*(9/5)+32

def convert_from_fahrenheit_to_kelvin(fah):
    return (fah - 32)*5/9 +273.15

def convert_from_kelvin_to_fahrenheit(kel):
    return (kel - 273.15)*9/5+32

play = True
while play:
    try:
        val = float(input("Enter the temperature value :"))
        unit = input("Enter the unit : \ncelsiuc : c\nkelvin : k\nfahenheit : f\n (or q to quit)")

        print(f"Entered temperature : {val} {unit}")
        if unit == 'c':
            print(f"Temperature in Farhenheit: {convert_from_celsius_to_fahrenheit(val)}")
            print(f"Temperature in Kelvin: {convert_from_celcius_to_kelvin(val)}")
        elif unit == 'f':
            print(f"Temperature in Kelvin: {convert_from_fahrenheit_to_kelvin(val)}")
            print(f"Temperature in Celsius : {convert_from_fahrenheit_to_celsius(val)}")
        elif unit == 'k':
            print(f"Temperature in Farhenheit: {convert_from_kelvin_to_fahrenheit(val)}")
            print(f"Temperature in Celsius : {convert_from_kelvin_to_celcius(val)}")
        else:
            break
    except:
        print("Please enter proper temperature value.")
        select = input("Do you want to quit (yes/no)")
        if select == 'yes':
            play = False
