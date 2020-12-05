def area_of_triangle(x,y,z):
    s = (1/2)*(x+y+z)
    Area = (s*(s-x)*(s-y)*(s-z))**(1/2)
    return Area

a =float(input("Enter the value of base"))
b =float(input("Enter the value of height"))
c =float(input("Enter the value of lenght"))


print ("the area of a triangle is ",area_of_triangle(a,b,c))

