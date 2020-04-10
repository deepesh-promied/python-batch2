#Default Argument Values / Optional Arguments

def demoFunction(x,y=10,z=30):
    print(f'X = {x}')
    print(f'Y = {y}')
    print(f'Z = {z}')
    print('-'*12)
    print()

demoFunction(10,20)
demoFunction(30,45,65)
demoFunction(z=30,x=40)