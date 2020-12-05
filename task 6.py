def max_2 (x,y) :
    if x > y:
        return x
    else:
        return y
def max_3(x,y,z) :
    
    return max_2( x, max_2( y, z ) )

a =int(input("Enter the first value "))
b =int(input("Enter the second  value "))
c =int(input("Enter the third value "))

print(max_3(a, b, c))
