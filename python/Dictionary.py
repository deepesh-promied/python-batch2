# Dictionary

def demoFunction():
    print('From Dictionary')
    return 10

dc = {'name':'Python','class':'Java'}


print(dc)

print(dc['name'])
print(list(dc.values()))
print(list(dc.keys()))

for i,v in dc.items():
    print(i,v)

'''
dc.keys() #Returns Keys
dc.values() #returns Values
dc.items() # Returns Key Value Pair
'''
print(len(dc))
print('-'*10)

dc1 = {'10':[100,20,30],'20':'Java'}

print(dc1['10'])
print(dc1['20'])
dc1['30'] = demoFunction
print(dc1)
x = dc1['30']
y = x()
print(y)