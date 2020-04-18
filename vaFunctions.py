#Function with Variable number arguments

def vaFunction(x,y,*b): #variable b will be a tuple
    print('x: ',x)
    print('y: ',y)
    print('b: ', b)

def vaFunction1(x,y,*b,**c):
    print(x)
    print(y)
    print(b)
    print(c)

vaFunction(10,20,30,40,50)
vaFunction1(10,20,30,40,50,name='saransh',batch='Python')