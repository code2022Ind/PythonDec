a = int(input("Enter the first Number:"))

b = int(input("Enter the Second number:"))

try:
    print(a/b)

except ZeroDivisionError as e:
    print("Canont be divided by zero")

print("End of the program")

