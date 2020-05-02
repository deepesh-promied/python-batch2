# Google Code
lst = [2,2,4,5,7]
n = 8
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if (i==j):
            continue
        if lst[i]+lst[j]==n:
            print(lst[i],lst[j])
