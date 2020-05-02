#Function as Object
def demoFunction(x=10,y=20,z=30):
    print(f'X = {x}')
    print(f'Y = {y}')
    print(f'Z = {z}')
    print('-'*12)
    print()

def demoFunction3():
    print('Hello World')

def demoFunction2(x):
    x()

demoFunction2(demoFunction)
demoFunction2(demoFunction3)