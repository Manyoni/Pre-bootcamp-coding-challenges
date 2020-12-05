def counting_vowels(str):
    vowels=0
    for i in str:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
            print ("the vowels in this string :",i)
    print ("Total number of vowels in the string ",vowels)

counting_vowels("Hellow world")








