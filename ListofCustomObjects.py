class Student:
    def __init__(self,name='',age=0,subject=''):
        self.name = name
        self.age = age
        self.subject = subject
    
    # Getter and Setter for name
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    # Getter and Setter for age

    def getAge(self):
        return self.age
    
    def setAge(self,age):
        self.age=age

    #Getter and Setter for Subject

    def getSubject(self):
        return self.subject

    def setSubject(self,subject):
        self.subject = subject


s1 = Student('Divyansh',20,'Python')
s2 = Student('Anvi',20,'Java')
s3 = Student('Sarthak',20,'Data Science')
s4 = Student('Saransh',20,'PHP')

lstStudent = []

lstStudent.append(s1)
lstStudent.append(s3)
lstStudent.append(s2)
lstStudent.append(s4)


for v in lstStudent:
    print(v.getName(), v.getSubject())



lstStudent.append(Student('Deepesh',40,'Python'))

lstStudent[2].setSubject('Python')



for v in lstStudent:
    print(v.getName(), v.getSubject())

