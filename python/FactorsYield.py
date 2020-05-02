def numberFactor(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

for i in numberFactor(100):
    print(i,end=' ')

