# Single level inheritence

class Sample :
    
    def m1 (self) :
         print ("m1")

class Demo(Sample) :   # inherits the class sample
     def m2 (self):
          print("m2")

class Test:
     def m3(self):
          print("m3")

obj1 = Demo()
obj1.m1()
obj1.m2()

#Multilevel Inheritence
