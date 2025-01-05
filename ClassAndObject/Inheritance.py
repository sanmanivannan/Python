class Vehile():                     #Parent class
    def general_usage(self):
        print("general usage")

class Car(Vehile):                  #Inherited Child1 class
    def __init__(self):
        print("im a car")
        self.wheels = 4
        self.roof = True

    def specific(self):
        print("car specific usage")   

class Bike(Vehile):                 #Inherited Child2 class
    '''def __init__(self):
        print("im a bike")
        self.wheels = 2
        self.roof = False  '''              

    def specific(self):
        print("bike specific usage")

c = Bike()       
c.general_usage()
c.specific()

#================================================================================
#isinstance method
#=================
print(isinstance(c,Vehile))

#issubclass method
#=================
print(issubclass(Car,Vehile))