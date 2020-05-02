# Linear Search Implementation
nts = int(input("Enter the number to search "))
lst =  [10,30,12,34,16,19] 

'''
flag = 1 
for i in range(len(lst)):
    if lst[i] == nts:
        print(f"{nts} found at {i+1} position")
        flag = 1
        break

if flag==0:
    print(f"{nts} not found in list {lst}")
'''

for i in range(len(lst)):
    if lst[i] == nts:
        print(f"{nts} found at {i+1} position")
        break
else:
    print(f"{nts} not found in list {lst}")