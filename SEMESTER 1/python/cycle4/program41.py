triangle=lambda b,h:.5*b*h
rectangle=lambda l,b:l*b
square=lambda s:s*s
base=int(input("Enter Base"))
height=int(input("Enter Height"))
print("AREA OF TRIANGLE")
print(triangle(base,height))
length=int(input("Enter Length"))
breadth=int(input("Enter Breadth"))
print("AREA OF RECTANGLE")
print(rectangle(length,breadth))
side=int(input("Enter Side"))
print("AREA OF SQUARE")
print(square(side))
