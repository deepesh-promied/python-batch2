lst=[10,20,30,40,50]
plst=[]
for i in range(len(lst)):
    prod = 1
    for j in range(len(lst)):
        if i!=j:
            prod = prod*lst[j]
    plst.append(prod)

print(plst)
