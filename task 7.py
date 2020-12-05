def celcius_to_fah(x):
    fah =(x*9)/5+32
    return fah

a = float (input("Enter the number in celcius and convert to fah"))

print ("The converted  number in fahrenheit ",celcius_to_fah(a))


def fah_to_celcius(y):
    celcius=(y-32)*5/9
    return celcius

b = float (input ("Enter the number in fah and convert to celcius"))
print ("The converted  number in fahrenheit ",fah_to_celcius(b))