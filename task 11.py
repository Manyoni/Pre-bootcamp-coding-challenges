def counting_vowels(s1,s2):
    vowels=0
    for i in s1:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' and s1 == s2):
            vowels=vowels+1
            print ("the common  vowels in this string are  :",i)
    print ("Total number of vowels inboth strings is ",vowels)



a = str(input("Enter the first word to compare the vows "))
b = str(input("Enter the second letter to compare the vows"))

counting_vowels(a,b)


