#Tuple
# Mutable Data Type
# Immutable Data Type

lst = [10,20,30,40,50]
tup = (10,20,30,40,50)

for i in range(len(tup)):
    print(tup[i])

print(min(tup))

print(tup.count(10))

x = list(tup)
tx = tuple(x)

print(tup)
print(x)
print(tx)