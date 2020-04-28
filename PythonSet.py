# Data Structure : Set
# Set is a collection of unique elements of smiliar / different data types
# Sets are not indexed

setDemo = {4,5,6,7} #Direct Assignment
print(setDemo)

#set Constructor / method

setDemo1 = set((10,20,20,40,50)) # Using Set Constructor
print(setDemo1)

setDemo3 = set('Python programming')# Using Set Constructor
print(setDemo3)

setDemo4 = set(['Python Programming'])# Using Set Constructor
print(setDemo4)

setDemo5 = {'Python Programming','Java Programming',2,4,6,'6','ds!@#'} #Direct Assignment
print(setDemo5)

'''
Inserting Values in a Set
'''

# Inserting 1 Value
setDemo5.add(5)
setDemo5.add(6)
setDemo5.add('CPP')
print(setDemo5)

#Insering Multiple Values
setDemo5.update([3,14,15])
print(setDemo5)
setDemo5.update('Java')
print(setDemo5)

'''
Deleting Elements
'''

 # remove
 # discard
 # pop

setDemo5.remove(14)
print(setDemo5)
setDemo5.discard(70)
print(setDemo5)

print(setDemo5.pop())
print(setDemo5)

print(setDemo5.pop())
print(setDemo5)

'''
Printing Set
'''
for x in setDemo5:
    print(x,end=' ')
print()

print(len(setDemo5))

#Operations on Sets