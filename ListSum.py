#Program to print sum of all the values in a list

lst = [10,20,30,40,50]

sum = 0

for i in range(0,len(lst)):
    sum = sum + lst[i]

print("Sum of {} is {}".format(lst,sum))