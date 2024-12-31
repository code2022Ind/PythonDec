class Car:
    def __init__(self,color,max_speed,tyre_friction):
        self.color = color 
        self.max_speed = max_speed 
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction 
        self.is_engine_started = False 
        self.current_speed = 0

    
class Truck(Car):
    def __init__(self, color, max_speed, accelaration, tyre_friction,max_cargo_weight):
        super().__init__(color, max_speed, accelaration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0

    def sound_horn(self):
        if self.is_engine_started == "True" :
            print("Honk Honk")
        else :
            print("Car has not started yet")
    
    def load_cargo(self, cargo_weight) :
        if self.is_engine_started == "True":
            print("Cannot load cargo during motion")
            

        elif self.load+cargo_weight > self.max_cargo_weight:
            print("Cannot load cargo more than max limit:"{max_cargo_weight})

        else :
            self.load = self.load +cargo_weight

    def unload_cargo(self,cargo_weight):
        
        if self.is_engine_started:
            print("cannot unload cargo during motion")

        else:
            print("Cannot unload cargo during motion")
