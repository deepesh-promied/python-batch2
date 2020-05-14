#Collection Package
import collections
#Named Tuple
Student = collections.namedtuple('StudentDetails',['name','subject','marks'])
tup_1 = Student('Divyansh','Python',45)
tup_2 = Student('Saransh','Python',55)
tup_3 = Student('Anvi','Java',85)
print(tup_1)
print(tup_2[0])
print(tup_3[0])
