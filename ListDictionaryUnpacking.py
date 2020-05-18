#Unpack Dictionary
def demoFunction(a,b,c):
    print(a,b,c)

def demoFunction2(name,subject):
   print(name,subject)

lst = [10,20,30]
di = {'subject':'Python','name':'Divi'}
#a,b,*c = lst #List Unpacking
#demoFunction(lst[0],lst[1],lst[2])
demoFunction(*lst) #List Unacking demoFunction(lst[0],lst[1],lst[2])
#demoFunction2(di["name"],di["subject"])
demoFunction2(**di) #demoFunction2(name='divi',subject='Python')