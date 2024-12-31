"""
Problem statement:  
Get the input String from user and parse it to integer, if it is not a number it will throw  
number format exception Catch it and print "Entered input is not a valid format for an integer." 
or else print the square of that number. (Refer Sample Input and Output).  

Sample input and output 1:  
Enter an integer: 12 
The square value is 144 
The work has been done successfully 
Sample input and output 2: 
Enter an integer: Java 
Entered input is not a valid format for an integer. 
"""

class NumberFormatException(Exception):
    def __init__(self, message="Entered input is not a valid format for an integer."):
        self.message = message
        super().__init__(self.message)

class Sample:
    def __init__(self):
        self.user_input = input("Enter an integer: ")
        
    def number(self):
        try:
            number = int(self.user_input)
            if isinstance(number, int):
                number = number * number
                print("The square value is:", number)
        except :
            raise NumberFormatException()


obj1 = Sample()

try:
    obj1.number()
except NumberFormatException as e:
    print(e)



"""
Write a program that takes as input the size of the array and the elements in the array.  
The program then asks the user to enter a particular index and prints the element at that index.  
Index  starts from zero.  
This program may generate Array Index Out Of Bounds Exception  or NumberFormatException.   
Use exception handling mechanisms to handle this exception.  
"""
# Array Index Out Of Bounds Exception and NumberFormatException handling
try:
    user_input = int(input("Enter the number of elements in the array: "))
    array = []
    print("Enter the elements in the array:")
    for _ in range(user_input):
        array.append(int(input()))

    index = int(input("Enter the index of the array element you want to access: "))
    print(f"The array element at index {index} = {array[index]}")
    print("The array element successfully accessed")
except ValueError as e1:
    print("NumberFormatError")
except IndexError as e2:
    print("Array Index Out Of Bounds Exception")



"""
Write a Program to take care of Number Format Exception if user enters values other than  
integer for calculating average marks of 2 students. The name of the students and marks  
in 3 subjects are taken from the user while executing the program. 
In the same Program write your own Exception classes to take care of Negative values and  
values out of range (i.e. other than in the range of 0-100) 
"""
class NegativeValueException(Exception):
    """Custom exception for handling negative values."""
    def __init__(self, message="Negative values are not allowed."):
        self.message = message
        super().__init__(self.message)

class OutOfRangeException(Exception):
    """Custom exception for handling values out of range (0-100)."""
    def __init__(self, message="Values out of range (0-100) are not allowed."):
        self.message = message
        super().__init__(self.message)

def validate_marks(mark):
    if mark < 0:
        raise NegativeValueException()
    elif mark > 100:
        raise OutOfRangeException()

def main():
    try:
        students = []
        for i in range(2):
            name = input(f"Enter the name of student {i + 1}: ")
            marks = []
            for j in range(3):
                mark = int(input(f"Enter mark {j + 1} for {name}: "))
                validate_marks(mark)
                marks.append(mark)
            students.append((name, marks))

        for student in students:
            name, marks = student
            avg_marks = sum(marks) / len(marks)
            print(f"Average marks for {name}: {avg_marks}")

    except ValueError:
        print("Entered input is not a valid format for an integer.")
    except NegativeValueException as e:
        print(e)
    except OutOfRangeException as e:
        print(e)

if __name__ == "__main__":
    main()



"""
A student portal provides user to register their profile. During registration the system needs  
to validate the user should be located in India. If not the system should throw an exception. 
Step 1: Create a user defined exception class named “InvalidCountryException”. 
Step 2: Overload the respective constructors. 
Step 3: Create a main class “UserRegistration”, add the following method, 
registerUser– The parameter are String username,String userCountry and add the following logic, 
• if userCountry is not equal to  “India” throw a InvalidCountryException with the message  
“User Outside India  cannot be registered” 
• if userCountry is equal to  “India”,  print the message “User registration done successfully” 
Invoke the method registerUser from the main method with the data specified and see how the program behaves, 
Name Country Expected Output 
Mickey US InvalidCountryException should be thrown. 
 The message should be “User Outside India  cannot be registered” 
Mini India The message should be “User registration done successfully” 
Sample Input and Output 
"""

class InvalidCountryException(Exception):
    """Custom exception for handling invalid country registrations."""
    def __init__(self, message="User Outside India cannot be registered"):
        self.message = message
        super().__init__(self.message)

class UserRegistration:
    @staticmethod
    def register_user(username, user_country):
        if user_country.lower() != "india":
            raise InvalidCountryException()
        else:
            print("User registration done successfully")

# Testing the UserRegistration
try:
    UserRegistration.register_user("Mickey", "US")
except InvalidCountryException as e:
    print(e)

try:
    UserRegistration.register_user("Mini", "India")
except InvalidCountryException as e:
    print(e)

