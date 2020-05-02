#googleCode
import sys
lst = [2,2,4,5,7]
n = int(sys.argv[1])

low = 0
high = 4
flag = 0

while low<high:
    if lst[low]+lst[high] == n:
        flag = 1
        print(lst[low],lst[high])  
        if lst[low+1]+lst[high]==n:
            low = low + 1
        elif lst[low] + lst[high-1]==n:
            high = high -1
        else:
            low = low+1
            high = high-1
    elif lst[low]+lst[high] < n:
        low = low+1
    else:
        high = high-1

if flag == 0:
    print("No Pair Found")



