class EligibleError(Exception):
    def __init__(self,message):
        super()

class Sample:
    def test(self,age,percentage):
        if age <=17 or percentage <= 60:
            raise EligibleError ("Not Elligible for registation")
        else:
            print("Registration Success")

obj1 = Sample()

try:
    obj1.test(16,17)
except EligibleError as e:
    print("You can registered")

        