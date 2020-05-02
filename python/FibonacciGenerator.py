#Fibonacci 

def fibo(n):
    if(n>2):
        first = 0
        second = 1
        yield first
        yield second
        for i in range(3,n+1):
            third = first + second
            yield third 
            first,second = second,third


for i in fibo(10):
    print(i, end=' ')

# fibo(5)
#0 1 1 2 3