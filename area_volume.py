# Basic Area and Volume Calculator
#Calculator for finding: areas (square, rectangle, circle, triangle), volumes (sphere, rectangular prism, cube), and circumference of a circle.
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
