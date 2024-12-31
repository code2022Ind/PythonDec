#Level 1

Dog = {}
print("Empty Dictionary:",Dog)

#Add name, color, breed, legs, age to the dog dictionary
Dog = {
    "Name" : "Moti",
    "Color" : "Black & White",
    "Breed" : "Indian",
    "legs" : 4,
    "age" : 2
}

print("Printing Dictionary:",Dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary 
Student = {
    "first_name" : "Sayali",
    "last_name" : "Thange",
    "gender" : "Female",
    "age" : 22,
    "maritial_status" : "Single",
    "skills" : ["Smart","Beautiful","Nice","Kind"],
    "country" : "India",
    "city" : "Banglore",
    "Address" : "Ahmednagar"

}

print("Student Dict: ", Student)


#Get the length of the student dictionary 
length = len(Student)
print("Length of Student dict:", length)

#Get the value of skills and check the data type, it should be a list 
print("Skills:",Student["skills"])
print("Type of Skills: ",type("skills"))


#Modify the skills values by adding one or two skills 
Student["skills"].extend(["SQL", "C++"]) 
print("Modified skills:", Student["skills"])

#Get the dictionary keys as a list 
Dict_list = list(Student.keys())
print("Dictionary keys as a list:", Dict_list)


#Get the dictionary values as a list 
Dict_values = list(Student.values())
print("Dictionary values as a list:", Dict_values)



#Change the dictionary to a list of tuples using items() method 
Dict_items = list(Student.items())
print("Dictionary as a list of tuples:", Dict_items)


#Delete one of the items in the dictionary 
del Student["age"]
print("Age is deleted", Student)

#Delete one of the dictionaries
del Student 
