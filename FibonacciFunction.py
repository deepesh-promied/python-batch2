def fibo(len):
    first = 0
    second = 1
    if (len >= 2):
        print(first, end=' ')
        print(second,end=' ')
        for i in range(3,len+1):
            print(first + second, end=' ')
            first,second = second,first + second
    else:
        print("Invalid input")

len = int(input("Enter the number of elements: "))
fibo(len)