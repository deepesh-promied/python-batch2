#List Slicing
lst = [100,20,130,410,50]

print("Actual List")
print(lst)

print("-" * 10)

x = lst[:]
print(x)

x = lst[::-1]
print(x)

x = lst[2:]
print(x)

x = lst[:6]
print(x)

x = lst[2:4]
print(x)

x = lst[2::2]
print(x)

x = lst[0::2]
print(x)

x = lst[0:5:-1]
print(x)

x = lst[:4:3]
print(x)


