# Generators
# Yield Statement

def demoFunction():
    print('First Statement')
    yield 'Python'
    print('Second Statement')
    yield 'Java'
    print('Third Statement')
    yield 'CPP'
    print('Nodejs')

#x = demoFunction()
#x = list(demoFunction())
#print(x)

x=[]
for i in demoFunction():
    x.append(i)
print(x)


