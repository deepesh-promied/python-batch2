#Try Catch Block
try:
    a = 10
    b = 20
    print(a/b)
    fp=open('MARKS123.csv','r')
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
