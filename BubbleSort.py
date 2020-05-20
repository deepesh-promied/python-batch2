#Bubble Sort
lst = [5,3,3,2,1]
ii=0
oi=0
while True:
    check = 0
    oi=oi+1
    for j in range(len(lst)-1):
        ii=ii+1
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            check = 1
    if check == 0:
        break
print(oi,ii)
print(lst)

# Method 2 
ii=0
oi=0
lst = [5,3,3,2,1]
for i in range(len(lst)-1,0,-1):
    oi = oi+1
    for j in range(i):
        ii=ii+1
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            check = 1
print(lst)
print(oi,ii)