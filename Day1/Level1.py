# Declare Empty list
a1 = []
print("1. Declare Empty list: ",a1)

#Declare List with more than 5 items
a1 = [1,2,"Hello","Python",4,5,"Welcome"]
print("2. Declare List with more than 5 items : ",a1)

#Find the length of the list
length = len(a1)
print("3. Find the length of the list",length)

#Get Get the first item, the middle item and the last item of the list 
first_item = a1[0]
print("4. Get the first item: ",first_item)

middle_item = a1[len (a1) // 2]
print("The middle item: ",middle_item)

last_item = a1[-1]
print("last item of the list: ",last_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Sayali",22,165,"Single","Banglore"]
print("5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)",mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon. 
it_companies =["Facebook", "Google","Microsoft","Apple","IBM", "Oracle","Amazon"]
print("6 : ",it_companies)

#Print the number of companies in the list 
length = len(it_companies)
print("8. Print the number of companies in the list: ",it_companies)

#Print the first, middle and last company 
first_company = it_companies[0]
print("9. First company: ",first_company)

middle_company = it_companies[len(it_companies) // 2]
print("Middle Company: ",middle_company)

last_comapany = it_companies[-1]
print("Last_Company: ",last_comapany)

#Print the list after modifying one of the companies 
it_companies[2] = "TCS"
print("10.Print the list after modifying one of the companies: ",it_companies)

#Add an IT company to it_companies 
it_companies.append("Microsoft")
print("11. Add an IT company to it_companies : ",it_companies)

#Insert an IT company in the middle of the companies list 
it_companies.insert(len (it_companies) // 2 , "Infosys")
print("12. Insert an IT company in the middle of the companies list: ",it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!) 
it_companies[6] = it_companies[6].upper()
print("13. Change one of the it_companies names to uppercase (IBM excluded!) : ",it_companies)

#Join the it_companies with a string '#;  ' 
joined_string = '#;'.join(it_companies)
print("14. #Join the it_companies with a string '#;  ' ",joined_string)

#Check if a certain company exists in the it_companies list.
if "IBM" in it_companies: 
    print("Exist")
else:
    print( "15. Check if a certain company exists in the it_companies list: ","Not exist")

#Sort the list using sort() method 
it_companies.sort()
print("16. Sort the list using sort() method: ",it_companies)

#Reverse the list in descending order using reverse() method 
it_companies.reverse()
print("17. Reverse the list in descending order using reverse() method :",it_companies)

#Slice out the first 3 companies from the list 
it_company = it_companies[:3]
print("18.Slice out the first 3 companies from the list: ",it_company)

#Slice out the last 3 companies from the list 
it_company = it_companies[-3:]
print("19.Slice out the last 3 companies from the list : ",it_company)

#Slice out the middle IT company or companies from the list
it_company = it_companies[1:7]
print("20. Slice out the middle IT company or companies from the list: ",it_company)

#Remove the first IT company from the list 
it_companies.pop(0)
print("21.Remove the first IT company from the list: ",it_companies)

#Remove the middle IT company or companies from the list 
middle_company = len(it_companies) // 2
it_companies.pop(middle_company)
print("22.Remove the middle IT company or companies from the list: ",it_companies)

#Remove the last IT company from the list 
it_companies.pop()
print("23.#Remove the last IT company from the list: ",it_companies)

#Remove all IT companies from the list 
it_companies.clear()
print("24.Remove all IT companies from the list: ",it_companies)

#Destroy the IT companies list 
#del it_companies
print("25. Destroy the IT companies list: ",it_companies)

#Join the following lists: 
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB'] 
full_stack= front_end + back_end
print("26.Join the following lists: ",full_stack)

# Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux. 
index = full_stack.index("Redux") + 1 
full_stack.insert(index, "Python") 
full_stack.insert(index + 1, "SQL") 
print("27. ", full_stack)
