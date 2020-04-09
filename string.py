#inbuilt methods for String

strDemo = 'Python Programming'
strDemo1 = 'Pyt:hon: Programming'
print('-'*20)
print(strDemo)
print('-'*20)

#Lower Method
print("Lower Methods:")
print(strDemo.lower())
print(strDemo)
print('-'*10)

#Lower Method
print("Lower Methods:")
print(strDemo.upper())
print(strDemo)
print('-'*10)

#Split Method: String to List
print("Lower Methods:")
print(strDemo.split())
print(strDemo1.split(':'))
print('-'*10)

#Join Method: List to String
lstDemo = ['String','join','method']
strdemo2 = ' '.join(lstDemo) 
print(strdemo2)

#strip, lstrip and rstrip
strdemo3 = '    Demo String     '
print(strdemo3)
print(strdemo3.strip() + 'test')
print(strdemo3.rstrip() + 'test')
print(strdemo3.lstrip(' eD') + 'test')
print('www.wetransfer.com'.lstrip('w.e'))

# For Remaining inbuilt Methods check:
# https://docs.python.org/3/library/stdtypes.html#string-methods

strdemo4 = """This is a demo for 
multiline string
This is the third line 
this is the fourth line"""

print(strdemo4)