from abc import ABC,abstractmethod

class Accounts:
    def savings(self):
        print("Zero Balance Account")

class Loans(ABC):
    @abstractmethod
    def pl(self):
        print("Personal Loans")

class Final(Loans) :
    def pl(self) :
        print("Personal Loans")

obj1 = Final()
obj1.pl()