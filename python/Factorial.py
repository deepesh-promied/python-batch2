'''
#Program to calculate Factorial of a number
'''

n = int(input("Enter the number: "))
fact = 1

'''
for i in range(n,1,-1):
    fact =  fact*i
'''

i=n
while(i>1):
    fact = fact*i
    i = i-1

print("Factorial for number {} is {}".format(i,fact))