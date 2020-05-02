# Linear Search Implementation
nts = int(input("Enter the number to search "))
lst =  [12,30,12,34,12,19]
pos = []

for i in range(len(lst)):
    if lst[i] == nts:
        #print(f"{nts} found at {i+1} position")
        pos.append(i+1)

if len(pos) == 0:
    print(f"{nts} not found in list {lst}")
else:
    print(f"{nts} found at the following positions {pos}")

