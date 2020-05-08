class Vehicle:
    def __init__(self,tyre):
        self.tyre = tyre

    def getTyre(self):
        return self.tyre
    
    def setTyre(self,tyre):
        self.tyre=tyre   

class Car(Vehicle):
    def __init__(self,tyre):
        super().__init__(tyre)

class Bus(Vehicle):
    def __init__(self,tyre):
        super().__init__(tyre)

class Truck(Vehicle):
    def __init__(self,tyre):
        super().__init__(tyre) 

class Sedan(Car):
    def __init__(self):
        print('Sedan Constructor') 

c = Car(5)
print(c.__dict__)

c1 = Car(6)
print(c1.__dict__)
