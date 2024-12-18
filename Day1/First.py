a1 = [1,20,"welcome", "hello", 40]
b1 = [111,222,333]
print(a1)
 
a1.append(120) #Add value at the end of the list
print(a1)

a1.insert(2,560) #adding value at specified position
print(a1)

a1[3] = 50 #update or replace
print(a1)

a1.remove("hello")
print(a1)

a1.extend(b1) #concatenate 2 list
print(a1)

a1.pop() #remove any value from last
print(a1)