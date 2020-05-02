#Program to check if a number is prime or not

ntc = int(input("Enter the number: "))

flag = 0

if(ntc>1):
    for i in range(2,int(ntc/2)+1):
        if ntc%i == 0:
            flag = 1
            break 
    if flag==1:
        print("Number is not a prime number")
    else:
        print("Number is a prime number")
else:
    print("Not a Valid Number")