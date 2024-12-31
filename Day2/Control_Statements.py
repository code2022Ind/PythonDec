#Simple if Condition
a = 10
b = 20
if a > b :
    print("Greater") # need to pass a statement after if ... 


#If dont want to pass any statement after if
a = 10
b = 20
if a > b :
    pass # Used when you want to execute if condition but dont want to pass any statement.

#Else if

a = 10
b = 20
if a > b :
    print("Greater") 
elif a < b:
     print("Smaller")
elif a==b :
    print("Equal")
else:
    pass

#True if condition else False
print("True") if a==b else print("False")