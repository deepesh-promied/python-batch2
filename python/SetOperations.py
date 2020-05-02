'''
1. Union
2. Intersection 
3. Difference
'''

set1 = {5,2,1}
set2 = {2,4,5}

# Union of Set
set3 = set1.union(set2)
print(set3)
set4 = set1|set2 # Pipe Symbol for Union
print(set4)

#Intersection
set3 = set1.intersection(set2)
print(set3)
set4 = set1&set2 #Intersection
print(set4)

#Difference
set3 = set1.difference(set2)
print(set3)
set4 = set1-set2
print(set4)

set3 = set2.difference(set1)
print(set3)
set4 = set2-set1
print(set4)