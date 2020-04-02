ntc = int(input('Enter the Number '))

while(ntc > 1):
    flag = 0
    #for i in range(2,int(ntc/2)):
    #   if ntc%i == 0:
    #       flag = 1
    
    i = 2
    while(i<int(ntc/2)):
        if ntc%i==0:
            flag =1
        i = i+1

    if flag==0:
        print("{} is a prime number".format(ntc))
    else:
        print("{} is not a prime number".format(ntc))
    
    ntc = int(input('Enter the next Number '))
