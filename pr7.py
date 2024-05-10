#WAP to area of a circle, triangle, rectangle square
print(f"Select the fig to find its area:\na. Circle\nb. Triangle\nc. Rectangle\nd. Square")
import math
def circle():
    r = int(input("Enter the radius of the circle: "))
    area = math.pi*r*r
    return area

def triangle():
    h = int(input("Enter the height of the triangle: ")) 
    b = int(input("Enter the base of that traingle: "))
    area = 0.5*b*h
    return area

def rectangle():
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breadth of the rectangle: "))
    area = l*b
    return area

def square():
    s = int(input("Enter the side of the square: "))
    area = s*s
    return area

while True:
    choice = input("")
    if choice.upper() == "A":
        print (circle(), "unit sq.")
        break
    elif choice.upper() == "B":
        print (triangle(), "unit sq.")
        break
    elif choice.upper() == "C":
        print (rectangle(), "unit sq.")
        break
    elif choice.upper() == "D":
        print (square(), "unit sq.")
        break
    else:
        print ("Please select any one out of the given option")
        
