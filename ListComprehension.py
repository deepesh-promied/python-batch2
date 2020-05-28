#List Comprehension

x = [1,2,3,4,5]
lst = []
for i in x:
    if i%2==0:
        lst.append(i)
print(lst)

lst1 = [i 
        for i in x 
        if i%2==0]
print(lst1)

lst2 = [i**2 for i in x]
print(lst2)

lst2 = [i**2 for i in x if i%2!=0]
print(lst2)


x2 = [[1,2,3],[4,5,6],[7,8,9]]

lst3=[i
        for l in x2 
        for i in l]
print(lst3)

lst4 = [1 if i%2==0 else 0
        for l in x2
        for i in l]
print(lst4)

lst5 = [i 
        for l in x2
        for i in l
        if i%2==0]
print(lst5)
'''
lst6 = [l  

]'''
lst6 = [[1 if i%2==0 else 0 for i in j] for j in x2]
print(lst6)

for j in lst6:
    print(j)


lst6 = ([1 if i%2==0 else 0 for i in j] for j in x2)
for i in lst6:
    print(i)