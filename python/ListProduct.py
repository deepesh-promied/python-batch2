# Product of List elements
lst = [10,20,30,40,50] #len(lst)=> 5
prod = 1

i = 0
while (i < len(lst)):
    prod = prod * lst[i]
    i = i+1

print(prod)