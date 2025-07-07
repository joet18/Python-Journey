import math
x=9
#print(math.pi)
#print(math.e)
#print(math.sqrt(x))
#math artimatic excersise.1 calculate the circumfrance of a circle#

radius=float(input("Enter the radius of the circle: "))
circumference=2*math.pi*radius
print(f"The circumference of the circle with radius {radius} is {round(circumference, 2)}")
#math artimatic excersise.2 calculate the area of a circle#
radius=float(input("Enter the radius of the circle:"))
area=math.pi*radius**2
print(f"The area of the circle with radius{radius}is {round(area, 2)}")

#calculate the hypotenuse of a right triangle#
a=float(input("Enter Side A:"))
b=float(input("Enter Side B:"))
c=math.sqrt(pow(a, 2)+pow(b,2))
print(f"The hypotenuse of the triangle with sides {a} and {b} is {round(c, 2)}")
