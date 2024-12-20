# -*- coding: utf-8 -*-
"""Group5_dsc430project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YrVFiaB6F7QhY2Fmv6P9OoD8v4r5DDYI

# **Calculator Project**

For this project, we wanted to make a bunch of calculators that would be useful for everyday purposes and basic mathematical classwork.

Group Members (Contribution):

Aksheytha Chelikavada (Basic Arithmetic, Cone Volume, Total Sum of Coins)

Srilasya Ankireddypalle (Basic Area and Volume Calculator, Currency Conversion Calculator)

Juveiria Munawer (Temperature Conversion)

Nyla Morrison (Unit Conversions)

Brian Urban (Input A, B, and C Values for Quadratic Equation, Calculate Discriminant, Calculate the Value(s) of X)

# Input A, B and C Values for Quadratic Equation
"""

import numpy as np

print("\nQuadratic Equation: ax² + bx + c\n")
a = int(input('Input value for a: '))
b = int(input('Input value for b: '))
c = int(input('Input value for c: '))
print(f"\n{int(a)}x² + {int(b)}x + {int(c)}\n")
print("Quadratic Formula: x = [-b ± √(|b² - 4ac|)] / 2a")

"""# Calculate Discriminant"""

print(' ')
d1 = b**2
d2 = 4*a*c
d = d1 - d2
sqrtVal = np.sqrt(abs(d))
roundVal = round(sqrtVal, 3)
print("Discriminant Formula: √(|b² - 4ac|)\n")
print(f"√(|{int(b)}² - 4×{int(a)}×{int(c)}|) = √(|{int(d1)} - {int(d2)}|) = √(|{int(d)}|) = {int(sqrtVal)}")

"""# Calculate the Value(s) of X"""

if d > 0:
    print("\nRoots are real and different:\n")
    add = (-b + sqrtVal) / (2 * a)
    print(f"Addition: ({int(-b)} + {sqrtVal} / (2 × {int(a)}) = {float(add)}")
    sub = (-b - sqrtVal) / (2 * a)
    print(f"Substraction: ({int(-b)} - {sqrtVal} / (2 × {int(a)}) = {float(add)}")

elif d == 0:
    print("\nRoots are real and the same:\n")
    div1 = -b / (2 * a)
    print(f"Calculate: {int(-b)} / (2 × {int(a)}) = {float(div1)}")

else:
    print("\nRoots are complex:\n")
    div2 = -b / (2 * a)
    print(f"[{int(-b)} / (2 × {int(a)})] ± {float(roundVal)}i = {float(div2)} ± {float(roundVal)}i")

"""# Cone Volume

"""

import math

def coneVol(r, h):
  vol = (1/3)*(math.pi)*((r)**2)*(h)
  return vol

a = float(input("Please enter a radius: "))
b = float(input("Please enter a height: "))
c = coneVol(a, b)
print(f"The area of the cone is {c}")

"""# Basic Arithmetic

"""

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multi(a,b):
  return a * b

def div(a,b):
  if b != 0:
    return a/b
  else:
    return "Denominator cannot be 0!"

a = float(input("Please enter a value: "))
b = float(input("Please enter a value (If doing division, make sure this value is not 0): "))
c = input("Enter operation (Addition, Subtraction, Multiplication, Division): ")

if c == "Addition":
  print(add(a,b))
elif c == "Subtraction":
  print(subtract(a,b))
elif c == "Multiplication":
  print(multi(a,b))
elif c == "Division":
  print(div(a,b))
else:
  print("Invalid Operator")

"""# Total Sum of Coins

"""

def coins(quarters, dime, nickel, pennies):

  total = 0
  total = (quarters * 0.25) + (dime * 0.10) + (nickel * 0.05) + (pennies * 0.01)
  return total

q = int(input("How many quarters? "))
d = int(input("How many dimes? "))
n = int(input("How many nickels? "))
p = int(input("How many pennies? "))

t = round(coins(q, d, n, p),2)
print(f"Your total amount is ${t}")

"""## Unit Conversions"""

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "inches": {"inches": 1, "feet": 1 / 12, "meters": 0.0254, "centimeters": 2.54, "yards": 1 / 36, "kilometers": 2.54e-5, "miles": 1 / 63360, "millimeters": 25.4, "micrometers": 25400, "nanometers": 2.54e7},
        "feet": {"inches": 12, "feet": 1, "meters": 0.3048, "centimeters": 30.48, "yards": 1 / 3, "kilometers": 0.0003048, "miles": 1 / 5280, "millimeters": 304.8, "micrometers": 304800, "nanometers": 3.048e8},
        "meters": {"inches": 39.3701, "feet": 3.28084, "meters": 1, "centimeters": 100, "yards": 1.09361, "kilometers": 0.001, "miles": 0.000621371, "millimeters": 1000, "micrometers": 1e6, "nanometers": 1e9},
        "centimeters": {"inches": 0.393701, "feet": 0.0328084, "meters": 0.01, "centimeters": 1, "yards": 0.0109361, "kilometers": 1e-5, "miles": 6.2137e-6, "millimeters": 10, "micrometers": 10000, "nanometers": 1e7},
        "yards": {"inches": 36, "feet": 3, "meters": 0.9144, "centimeters": 91.44, "yards": 1, "kilometers": 0.0009144, "miles": 1 / 1760, "millimeters": 914.4, "micrometers": 914400, "nanometers": 9.144e8},
        "kilometers": {"inches": 39370.1, "feet": 3280.84, "meters": 1000, "centimeters": 100000, "yards": 1093.61, "kilometers": 1, "miles": 0.621371, "millimeters": 1e6, "micrometers": 1e9, "nanometers": 1e12},
        "miles": {"inches": 63360, "feet": 5280, "meters": 1609.34, "centimeters": 160934, "yards": 1760, "kilometers": 1.60934, "miles": 1, "millimeters": 1.609e6, "micrometers": 1.609e9, "nanometers": 1.609e12},
        "millimeters": {"inches": 0.0393701, "feet": 0.00328084, "meters": 0.001, "centimeters": 0.1, "yards": 0.00109361, "kilometers": 1e-6, "miles": 6.2137e-7, "millimeters": 1, "micrometers": 1000, "nanometers": 1e6},
        "micrometers": {"inches": 3.93701e-5, "feet": 3.2808e-6, "meters": 1e-6, "centimeters": 1e-4, "yards": 1.0936e-6, "kilometers": 1e-9, "miles": 6.2137e-10, "millimeters": 0.001, "micrometers": 1, "nanometers": 1000},
        "nanometers": {"inches": 3.93701e-8, "feet": 3.2808e-9, "meters": 1e-9, "centimeters": 1e-7, "yards": 1.0936e-9, "kilometers": 1e-12, "miles": 6.2137e-13, "millimeters": 1e-6, "micrometers": 0.001, "nanometers": 1}
    }

    #Makes sure units are in dictionary
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        return "Invalid units! Please use 'inches', 'feet', 'meters', or 'centimeters'."

    # Performs conversion
    result = value * conversion_factors[from_unit][to_unit]
    return result

#User input for conversion
value = float(input("Enter the value to convert: "))
from_unit = input("Enter the unit to convert from (inches, feet, meters, centimeters): ").lower()
to_unit = input("Enter the unit to convert to (inches, feet, meters, centimeters): ").lower()

converted_value = convert_units(value, from_unit, to_unit)
if isinstance(converted_value, str):
    print(converted_value)  # Output error if units are invalid
else:
    print(f"{value} {from_unit} is equal to {converted_value} {to_unit}")

"""# Basic Area and Volume Calculator
Calculator for finding: areas (square, rectangle, circle, triangle), volumes (sphere, rectangular prism, cube), and circumference of a circle.

"""

import math

def squarea(x):
    return x * x

def rectarea(l, w):
    return l * w

def triarea(b, h):
    return 0.5 * b * h

def circarea(r):
    return math.pi * r * r

def circumf(r):
    return 2 * math.pi * r

def cube_vol(x):
    return x**3

def rect_vol(l, w, h):
    return l * w * h

def sphere_vol(r):
    return (4/3) * math.pi * r**3

def cyl_vol(r, h):
    return math.pi * r * r * h

def av_calculator():
    print("Choose a calculation:")
    print("1. Square (Area)")
    print("2. Rectangle (Area)")
    print("3. Triangle (Area)")
    print("4. Circle (Area)")
    print("5. Circle (Circumference)")
    print("6. Cube (Volume)")
    print("7. Rectangle (Volume)")
    print("8. Sphere (Volume)")
    print("9. Cylinder (Volume)")

    choice = int(input("Choice (1-9): "))

    if choice == 1:
        x = float(input("Side length: "))
        print("Area of square:", squarea(x))

    elif choice == 2:
        l = float(input("Rectangle length: "))
        w = float(input("Rectangle width: "))
        print("Area of rectangle:", rectarea(l, w))

    elif choice == 3:
        b = float(input("Triangle base: "))
        h = float(input("Triangle height: "))
        print("Area of triangle:", triarea(b, h))

    elif choice == 4:
        r = float(input("Circle radius: "))
        print("Area of circle:", circarea(r))

    elif choice == 5:
        r = float(input("Circle radius: "))
        print("Circumference of circle:", circumf(r))

    elif choice == 6:
        x = float(input("Side length: "))
        print("Volume of cube:", cube_vol(x))

    elif choice == 7:
        l = float(input("Rectangle length: "))
        w = float(input("Rectangle width: "))
        h = float(input("Rectangle height: "))
        print("Volume of rectangle:", rect_vol(l, w, h))

    elif choice == 8:
        r = float(input("Sphere radius: "))
        print("Volume of sphere:", sphere_vol(r))

    elif choice == 9:
        r = float(input("Cylinder radius: "))
        h = float(input("Cylinder height: "))
        print("Volume of cylinder:", cyl_vol(r, h))

    else:
        print("Select a number between 1 and 9.")
        av_calculator()

av_calculator()

"""# Currency Conversion Calculator
Convert the USD into one of these currencies:
MXN, EUR, GBP, CHF, JPY, KRW, CNY, or INR.
"""

def usd_to_currency(usd, rate):
    return usd * rate

def currency_converter():
    rates = {"MXN": 20.4, "EUR": 0.94, "GBP": 0.78, "CHF": 0.88, "JPY": 154.03, "KRW": 1401.44, "CNY": 7.23, "INR": 84.4}

    print("USD Currency Converter")
    usd = float(input("Enter amount of USD: "))

    print("Choose a currency:")
    print("1. Mexican Peso (MXN)")
    print("2. Euro (EUR)")
    print("3. British Pound (GBP)")
    print("4. Swiss Franc (CHF)")
    print("5. Japanese Yen (JPY)")
    print("6. Korean Won (KRW)")
    print("7. Chinese Yuan (CNY)")
    print("8. Indian Rupee (INR)")

    choice = int(input("Choice (1-8): "))

    codes = list(rates.keys())

    if 1 <= choice <= 8:
        selection = codes[choice - 1]
        rate = rates[selection]
        converted = usd_to_currency(usd, rate)
        print(f"{usd} USD is equivalent to {converted:.2f} {selection}")
    else:
        print("Please select a number between 1 and 8.")
        currency_converter

currency_converter()

"""# Temperature Conversion Calculator
Convert the Celsius temperature into following :
Farenheit, Kelvin, Rankine
"""

#Step 1:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Step 2:
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Step 3:
def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 9/5

# Step 4:
def display_menu():
    print("\nTemperature Conversion Options:")
    print("1: Convert to Fahrenheit")
    print("2: Convert to Kelvin")
    print("3: Convert to Rankine")
    print("4: Exit")

#Step 5:
def perform_conversion(celsius, choice):
    if choice == '1':
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\n{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == '2':
        kelvin = celsius_to_kelvin(celsius)
        print(f"\n{celsius}°C is equal to {kelvin} K.")
    elif choice == '3':
        rankine = celsius_to_rankine(celsius)
        print(f"\n{celsius}°C is equal to {rankine}°R.")
    else:
        print("Invalid choice. Please try again.")

# Step 6:
def temperature_conversion_calculator():
    print("Welcome to the Temperature Conversion Calculator!")

    while True:
        try:
            celsius = float(input("\nEnter the temperature in Celsius (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for Celsius temperature.")
            continue

        while True:
            display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '4':
                print("Exiting the calculator. Goodbye!")
                return
            elif choice in ['1', '2', '3']:
                perform_conversion(celsius, choice)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Step 7: Get results by running the temperature conversion calculator
temperature_conversion_calculator()

"""Convert the Farenheit temperature into following :
Celsius, Kelvin, Rankine
"""

# Step 1:
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Step 2:
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

# Step 3:
def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

# Step 4:
def display_menu():
    print("\nTemperature Conversion Options:")
    print("1: Convert to Celsius")
    print("2: Convert to Kelvin")
    print("3: Convert to Rankine")
    print("4: Exit")

# Step 5:
def perform_conversion(fahrenheit, choice):
    if choice == '1':
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{fahrenheit}°F is equal to {celsius}°C.")
    elif choice == '2':
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"\n{fahrenheit}°F is equal to {kelvin} K.")
    elif choice == '3':
        rankine = fahrenheit_to_rankine(fahrenheit)
        print(f"\n{fahrenheit}°F is equal to {rankine}°R.")
    else:
        print("Invalid choice. Please try again.")

# Step 6:
def temperature_conversion_calculator():
    print("Welcome to the Fahrenheit Temperature Conversion Calculator!")

    while True:
        try:
            fahrenheit = float(input("\nEnter the temperature in Fahrenheit (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for Fahrenheit temperature.")
            continue

        while True:
            display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '4':
                print("Exiting the calculator. Goodbye!")
                return
            elif choice in ['1', '2', '3']:
                perform_conversion(fahrenheit, choice)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Step 7: Get results by running the temperature conversion calculator
temperature_conversion_calculator()

"""Convert the Kelvin temperature into following :
Celsius, Farenheit, Rankine
"""

# Step 1:
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Step 2:
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Step 3:
def kelvin_to_rankine(kelvin):
    return kelvin * 9/5

# Step 4:
def display_menu():
    print("\nTemperature Conversion Options:")
    print("1: Convert to Celsius")
    print("2: Convert to Fahrenheit")
    print("3: Convert to Rankine")
    print("4: Exit")

# Step 5:
def perform_conversion(kelvin, choice):
    if choice == '1':
        celsius = kelvin_to_celsius(kelvin)
        print(f"\n{kelvin} K is equal to {celsius}°C.")
    elif choice == '2':
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"\n{kelvin} K is equal to {fahrenheit}°F.")
    elif choice == '3':
        rankine = kelvin_to_rankine(kelvin)
        print(f"\n{kelvin} K is equal to {rankine}°R.")
    else:
        print("Invalid choice. Please try again.")

# Step 6:
def temperature_conversion_calculator():
    print("Welcome to the Kelvin Temperature Conversion Calculator!")

    while True:
        try:
            kelvin = float(input("\nEnter the temperature in Kelvin (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for Kelvin temperature.")
            continue

        while True:
            display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '4':
                print("Exiting the calculator. Goodbye!")
                return
            elif choice in ['1', '2', '3']:
                perform_conversion(kelvin, choice)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Step 7: Getting the results by running the temperature conversion calculator
temperature_conversion_calculator()

"""Convert the Rankine temperature into following :
Celsius, Farenheit, Kelvin
"""

# Step 1:
def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5/9

# Step 2:
def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

# Step 3:
def rankine_to_kelvin(rankine):
    return rankine * 5/9

# Step 4:
def display_menu():
    print("\nTemperature Conversion Options:")
    print("1: Convert to Celsius")
    print("2: Convert to Fahrenheit")
    print("3: Convert to Kelvin")
    print("4: Exit")

# Step 5:
def perform_conversion(rankine, choice):
    if choice == '1':
        celsius = rankine_to_celsius(rankine)
        print(f"\n{rankine}°R is equal to {celsius}°C.")
    elif choice == '2':
        fahrenheit = rankine_to_fahrenheit(rankine)
        print(f"\n{rankine}°R is equal to {fahrenheit}°F.")
    elif choice == '3':
        kelvin = rankine_to_kelvin(rankine)
        print(f"\n{rankine}°R is equal to {kelvin} K.")
    else:
        print("Invalid choice. Please try again.")

# Step 6:
def temperature_conversion_calculator():
    print("Welcome to the Rankine Temperature Conversion Calculator!")

    while True:
        try:
            rankine = float(input("\nEnter the temperature in Rankine (or type 'exit' to quit): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for Rankine temperature.")
            continue

        while True:
            display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '4':
                print("Exiting the calculator. Goodbye!")
                return
            elif choice in ['1', '2', '3']:
                perform_conversion(rankine, choice)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# Step 7: Getting the results by running the temperature conversion calculator
temperature_conversion_calculator()