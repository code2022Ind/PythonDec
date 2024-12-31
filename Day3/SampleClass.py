class Sample:
    a = 10
    name = "Sayali"
    def m1(self):
        print("m1")
    def m2(self):
        self.m1()

obj = Sample()
print(obj.a)
obj.m1()



class Sample:
    a = 10
     
    def m1(self):
        print("Calling m1")
    
    def __init__(self):
        print("Constructor calling")
        