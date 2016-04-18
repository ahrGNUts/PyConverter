#!/usr/bin/python

# this program should display a menu and convert input into whatever the function calls for


def show_menu():
    print "Welcome to the converter system."
    print "Choose a conversion from below by typing its corresponding number:"
    print "1. Celsius to Fahrenheit"
    print "2. Pounds to Kilograms"
    print "3. Feet to Kilometers"

    return int(raw_input('Choice: '))

def value_input(conversion_type):
    if conversion_type == 1:
        val = float(raw_input('Enter degrees in Celsius to convert: '))
        celsius_to_fahrenheit(val)
    elif conversion_type == 2:
        val = float(raw_input('Enter pounds to convert to kilograms: '))
        pounds_to_kilos(val)
    elif conversion_type == 3:
        val = float(raw_input('Enter feet to convert to kilometers: '))
        feet_to_km(val)
    else:
        print "Invalid entry. Now exiting..."

def celsius_to_fahrenheit(input):
    # stuff happens

def pounds_to_kilos(input):
    # other stuff happens

def feet_to_km(input):
    # yet different stuff happens

def main():
    choice = show_menu()
