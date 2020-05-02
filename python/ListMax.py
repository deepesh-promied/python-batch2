#Write a program to find max value in a list
lst = [100,20,30,14,56]
min = lst[0]
max = lst[0]

for i in range(1,len(lst)):
    if(max < lst[i]):
        max = lst[i]
    if(min > lst[i]):
        min = lst[i]

print(f"{max} is the max value and {min} is the minimum value in the list {lst}")