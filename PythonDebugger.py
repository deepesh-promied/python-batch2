import pdb

def calculateProduct(lst):
    prod = 1
    for v in lst:
        prod = prod * v
    return prod

pdb.set_trace()

x = [1,2,3,4,5]
sum = 0
for v in x:
    sum = sum +v

prod = calculateProduct(x)
print(prod)

'''
Dubugging Commands
next
step
until
cont
''''
