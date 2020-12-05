def convert_num_into_time (x):
    
    hour = int(x/60)
    minutes =x%60  
    return (hour,minutes)
    

time = float(input("Enter a number and convet it to hours and minutes"))
print ("Hours : minutes",convert_num_into_time(time))
