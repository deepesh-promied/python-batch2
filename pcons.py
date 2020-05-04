#parameterized Constructor

class Student:
    #Fees (Already added)
    #Name
    #Class
    #dateofbirth
    #age
    def __init__(self,f=0): #Constructor
        #print("Object Created. This is a message from constructor")
        self.fees = f
        
    def payFees(self,amount):
        self.fees = self.fees + amount
    
    def getFees(self):
        return self.fees

    def __del__(self): #Destructor 
        #print('Destructor')
        pass

st = Student()
st1 = Student(1000)
st2 = Student(2000)

print(st.getFees())
print(st1.getFees())
print(st2.getFees())

print(st.fees)
st.fees = 5000
print(st.getFees())
print(st1.getFees())
print(st2.getFees())