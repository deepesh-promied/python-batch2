#Fibonacci 

def fibo(n):
    lst = []
    if(n>2):
        first = 0
        second = 1
        lst.append(first)
        lst.append(second)
        for i in range(3,n+1):
            third = first + second
            lst.append(third)
            first,second = second,third
    return lst

#print(fibo(10))

for i in fibo(10):
    print(i, end=' ')
