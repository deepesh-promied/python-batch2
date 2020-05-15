#Collection Package
import collections

#Named Tuple
#Student = collections.namedtuple('Student',['name','subject','marks'])
#Student = collections.namedtuple('Student',('name','subject','marks'))

Student = collections.namedtuple('Student','name subject marks')
tup_1 = Student('Divyansh','Python',45)
tup_2 = Student('Saransh','Python',55)
tup_3 = Student('Anvi','Java',85)

#print(tup_1)
#Accessing Attributes
print(tup_1[0])
print(tup_1.name)
print(getattr(tup_1,'name'))

print(tup_1._fields) # Fields -- Tuple of Fields

tup4 = tup_1._replace(subject='Java',name='Deepesh') #To Create a Copy after replacing values provided
print(tup4)


'''
Creating Named Tuple from List or Tuple or Dictionary
'''

lst = ['Ajay','Python',45]
di = {'name':'Vijay','subject':'Python','marks':55}

tup5 = Student._make(lst) # Creating Named Tuple from List
tup6 = Student(**di) # Creating Named Tuple from Dictionary

print(tup5)
print(tup6)