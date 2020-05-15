#Default Dictionary from Collections Package.
from collections import defaultdict
def demoFunction():
    return 'Not Defined'


di = {'name':'Ajay','subject':'Python'}
#print(di['marks'])

d = defaultdict(demoFunction)
d['name'] = 'Divyansh'
d['marks'] = 45
print(d)
print(d['name'])
print(d['marks'])

#Assignment: How to create defaultdictionary from a dictionary