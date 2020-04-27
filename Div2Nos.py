x = list(map(int, input("Enter a multiple value: ").split())) 

try:
    p = x[0] / x[1]
    print(p)

except ZeroDivisionError:
    print('Zero Division')

except TypeError:
    print('Type Error')

except FileNotFoundError:
    print("No File Found!")

else:
    print('Else Block')

finally:
    print('Finally')