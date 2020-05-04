#Object Oriented Programming (OOPs)
class Student:
    def __init__(self): #Constructor
        print("Object Created. This is a message from constructor")
        self.fees = 0
        
    def payFees(self,amount):
        self.fees = self.fees + amount
    
    def getFees(self):
        return self.fees

    def __del__(self): #Destructor 
        print('Destructor')
        

st = Student()
st2 = Student()
print(st.getFees())
print(st2.getFees())

st.payFees(1000)
st2.payFees(2000)

print(st.getFees())
print(st2.getFees())

st.payFees(5000)
print(st.getFees())
print(st2.getFees())