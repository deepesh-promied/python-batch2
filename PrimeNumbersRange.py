#program to list all prime numbers in the given range
lowerlimit = int(input("enter the starting value: "))
upperlimit = int(input("Enter the ending value: "))

if(lowerlimit > 1 and upperlimit>lowerlimit):
    #Loop to travrse all the values in the range
    for ntc in range(lowerlimit,upperlimit+1):
        
        flag = 0
        #loop to check every value in the range

        for i in range(2,int(ntc/2)): 
            if ntc%i == 0:
                flag = 1
                break
                 
        if flag==0:
            print("{} is a prime number".format(ntc))        
else:
    print("Invalid range values")