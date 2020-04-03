'''
Write a program to print sum of all the numbers up to n. 
Value of n is entered by user.
'''

n = int(input("Enter the number: "))
total = 0
#n=5
'''
for i in range(1,n+1):
    total = total + i
    #total: 15 
'''
i=1
while(i<=n):
    total = total + i
    i = i + 1

print("Sum of all the numbers till {} is {}".format(n,total))