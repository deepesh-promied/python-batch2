import random
class Student:
    pass

class Student1(Student):
    pass

def getRandom():
    return random.randint(1,10)

def checkPercentage(x):
    if x>=0 and x<=100:
        return True
    else:
        return False

def checkObject():
    return

def returnStudent():
    return Student1()

if __name__ == '__main__':
    print(getRandom())
    print(getRandom())
