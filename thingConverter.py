#!/usr/bin/python

# this program displays a menu and converts input into whatever the function calls for


def show_menu():
    print "Welcome to the converter system."
    print "Choose a conversion from below by typing its corresponding number:"
    print "1. Celsius to Fahrenheit"
    print "2. Pounds to Kilograms"
    print "3. Feet to Kilometers"

    return input('Choice: ')


def value_input(conversion_type):  # get whatever value is going to be converted, call conversion function
    if conversion_type == 1:
        val = input('Enter degrees in Celsius to convert: ')
        celsius_to_fahrenheit(val)
    elif conversion_type == 2:
        val = input('Enter pounds to convert to kilograms: ')
        pounds_to_kilos(val)
    elif conversion_type == 3:
        val = input('Enter feet to convert to kilometers: ')
        feet_to_km(val)
    else:
        print "Invalid entry. Now exiting..."


def celsius_to_fahrenheit(c_degrees):
    f_degrees = c_degrees * 1.8 + 32  # conversion calculation
    print str(c_degrees) + ' C = ' + str(f_degrees) + ' F'  # output, end


def pounds_to_kilos(pounds):
    kilos = pounds / 2.2046226218  # conversion calculation
    print '%.2f' % pounds + ' lb(s) = ' + '%.2f' % kilos + ' kg(s)'  # output, end


def feet_to_km(feet):
    km = feet * 0.0003048  # conversion calculation
    print '%.2f' % feet + ' ft = ' + '%.2f' % km + ' km'  # output, end


def main():
    choice = show_menu()  # call menu, get user choice
    value_input(choice)  # user enters n units to be converted, conversion function called, output, end program

main()  # run
