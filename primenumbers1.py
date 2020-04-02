#Program to check if a number is prime or not

ntc = int(input("Enter the number: "))
if(ntc>1):
    for i in range(2,int(ntc/2)):#2,3,4
        if ntc%i == 0:
            break
    else:#Excuted if break is not ever executed in the loop
        print("Number is a prime number")
else:
    print("Not a Valid Number")