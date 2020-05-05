class Student:
    def __init__(self,name='',marks=0,subject='',gender='Female'):
        self.name = name
        self.gender = gender
        self.marks = marks
        self.subject = subject
    
    # Getter and Setter for name
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    # Getter and Setter for age

    def getMarks(self):
        return self.marks
    
    def setMarks(self,marks):
        self.marks=marks

    #Getter and Setter for Subject

    def getSubject(self):
        return self.subject

    def setSubject(self,subject):
        self.subject = subject

    #Getter and Setter for Gender
    def getGender(self):
        return self.gender

    def setGender(self,gender):
        self.gender = gender

lstStudent = []

with open('./Data/File1.csv','r') as fp:
    for line in fp:
        data = line.strip().split(',')
        lstStudent.append(Student(data[0],data[3],data[2],data[1]))

print(len(lstStudent))

for i in range(0,50):
    print(lstStudent[i].getName())

lstStudent.sort(key=self.getMarks())