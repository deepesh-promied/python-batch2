#Accessing list using negative indices

lst = [10,20,30,40,50] #len(lst)=> 5

for i in range(-1,-len(lst)-1,-1):
    print(lst[i])

i = -1
while(i>=-len(lst)):
    print(lst[i])
    i = i-1    
