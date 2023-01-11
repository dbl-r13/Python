#!/usr/bin/env python3

choice = int(input("Press 1 to convert Fahrenheit to Celsius, press 2 to conver Celsius to Fahrenheit "))

if choice == 1:
	temp = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))
	celsius = round((temp - 32) * 5 / 9, 2)
	print(f"{temp} F is {celsius} C")
elif choice == 2:
	temp = float(input("What temperature (in Celsius) would you like converted to Fahrenheit? "))
	print(choice)
	print("Still working in this") 
else:
	print("Invalid Input, please select again")


