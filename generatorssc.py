#Generator Shortcut
lst = [12,34,56,78,90]


x = list((i*2 for i in lst)) # Generator Object
y = tuple([i*2 for i in lst]) #List Comprehension

print(x)
print(y)

for v in x:
    print (v)

