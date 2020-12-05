def compare_two_numbers(x,y):
    if x==3 or y == 3 and (x+y)  == 3:
        return True
    else:
        return False

a = int(input("Please enter the first number input a whole number"))
b = int(input("Please enter the second number input a whole number"))

compare_two_numbers(a,b)
