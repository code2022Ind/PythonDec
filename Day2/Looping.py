#Simple i
for i in range(1,51) :
    print(i)

# For loop with break & continue
for i in range(1,51) :
    if i%5 ==0:
        continue
    print(i) #It will print all the numbers except divisible by 5


    for i in range(1,51) :
        if i%5 ==0:
            break
    print(i) #It will print all the number up to 4

    for i in range(1,51) :
        if i % 5 == 0 :
            print(i) # It will print all the divisible of 5 like 5,10,15 etc etc

    #Using for loop for dictionary
    a1 = {
        101 : "Sayali",
        102 : "Alfiya",
        103 : "Sandhya",
        104 : "Vedantika"
    }

    for i in a1 :
        print(i) # This will print only key like 101,102

    #To print key value pair
    for key,value in a1.items():
        print(key,value)  #This will print all the key with value