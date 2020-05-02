#Inbuilt Methods
lst = [100,20,30,14,56]
print('-'*20)
print(lst)
print('-'*20)

# Append Method
print("Append Method")
lst.append(20)
print(lst)
print('-'*10)

# Count Method
print("Count Method")
x = lst.count(20)
print(x)
print('-'*10)

# max Function
print("Max Function")
x = max(lst)
print(x)
print('-'*10)

# min Function
print("Min Function")
x = min(lst)
print(x)
print('-'*10)

# Sum Function
print("Sum Function")
x = sum(lst)
print(x)
print('-'*10)

# Insert Method
print("Insert Method")
lst.insert(2,36)
print(lst)
lst.insert(50,45)
print(lst)
lst.insert(-50,25)
print(lst)
print('-'*10)

#Remove Method
print("Remove Method")
lst.remove(20)
print(lst)
print('-'*10)

#Pop Method
print("Pop Method")
lst.pop(2)
print(lst)
print('-'*10)

#Reverse String
print("Reverse Method")
lst.reverse()
print(lst)
print('-'*10)

#Sort Methods
print("Sort Method")
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print('-'*10)
