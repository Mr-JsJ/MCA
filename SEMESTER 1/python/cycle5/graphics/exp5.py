from rectangle import area as rectArea
from rectangle import perimeter as rectPerimeter
from circle import perimeter as circlePerimeter
from circle import area as circleArea
from ThreeD.cuboid import *
from ThreeD.sphere import *
length=int(input("Enter the length of rectangle:"))
breadth=int(input("Enter the breadth of rectangle:"))
radius=int(input("Enter radius of circle:"))
l=int(input("Enter the length of cuboid:"))
w=int(input("Enter the width of cuboid:"))
h=int(input("Enter the height of cuboid:"))
r=int(input("Enter radius of sphere:"))
a1=rectArea(length,breadth)
a2=circleArea(radius)
p1=rectPerimeter(length,breadth)
p2=circlePerimeter(radius)
sa1=surface_area(l,w,h)
v1=volu_me(l,w,h)
sa2=surfaceArea(r)
v2=volume(r)
print("Area of raectangle",a1)
print("Perimeter of rectangle:",p1)
print("Area of circle",a2)
print("Perimeter of circle:",p2)
print("Surface Area of cuboid",sa1)
print("volume of cuboid",v1)
print("Surface Area of sphere",sa2)
print("volume of sphere",v2)


