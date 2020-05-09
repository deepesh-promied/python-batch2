class Vehicle():
    VehicleCount = 0    
    def __init__(self,tyre=0):
        self.tyre = tyre
        self._bootspace = 100
        self.__tyre_size = 50
        Vehicle.VehicleCount +=1

    def getTyre(self):
        return self.tyre
    
    def getTyreSize(self):
        return self.__tyre_size
    
    def setTyre(self,tyre):
        self.tyre=tyre
    
    def __str__(self):
        return f'Vehicle Object With Tyre Size {self.getTyre()}'

    def __repr__(self):
        return f'Vehicle Representation'
    
    def __demoMethod(self):
        return 'Vehicle Class'
       
    @classmethod #decorator
    def getVehicleCount(cls):
        return cls.VehicleCount
    
    @staticmethod
    def getVehicleCount1():
        return 'Static Method'

class Car:
    def __init__(self):
        pass
    
    def __demoMethod(self):
        return 'Car Class'

class Sedan(Car,Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        Car.__init__(self)
    
#v = Vehicle()
#print(dir(v))
#x = str(v) # v.__str__
#x = v
#print(v._bootspace)
#v1 = str(v)
#print(v.__dict__)
#print(v.__tyre_size) # Error
#print(v.getTyreSize())
#print(dir(v))

s = Sedan()
print(s._Car__demoMethod())
print(s._Vehicle__demoMethod())

print(Vehicle.getVehicleCount())
Vehicle.getVehicleCount1()