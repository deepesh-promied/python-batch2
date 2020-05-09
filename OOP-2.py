class Vehicle:
    VehicleCount = 0
    def __init__(self,tyre=0):
        self.tyre = tyre
        Vehicle.VehicleCount +=1

    def getTyre(self):
        return self.tyre
    
    def setTyre(self,tyre):
        self.tyre=tyre
    
    @classmethod #decorator
    def getVehicleCount(cls):
        return cls.VehicleCount   
      
class Sedan:
    def __init__(self,bootspace):
        self.bootspace = bootspace
        
    
    def getTyre(self):
        return self.bootspace

class Car(Vehicle,Sedan):
    def __init__(self,tyre,bootspace):
        Sedan.__init__(self,bootspace)
        Vehicle.__init__(self,tyre)

    def getTyre(self,x):
        if(x==1):
            return Sedan.getTyre(self)
        else:
            return Vehicle.getTyre(self)

class Bus(Vehicle):
    def __init__(self):
        super().__init__()
    
    #Function Overriding
    
    '''
    def getTyre(self,spare):
        return self.tyre+spare #Including extra wheel
    '''

print('Vechile', Vehicle.getVehicleCount())
c = Car(10,250)
print(Car.VehicleCount)
print('Car',c.getVehicleCount())
b = Bus()
print('Bus',b.getVehicleCount())
print(Car.VehicleCount)



