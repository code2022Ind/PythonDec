#Level 1

A = ()
print("Empty tuple:",A)
print("Print the empty list:",A)

Sister = ("Sayali","Gauri")
Brother = ("Jaydeep", "Saideep")
print("Sister:",Sister)
print("Brother:",Brother)

Siblings = Sister + Brother
print("Siblings:",Siblings)

length = len(Siblings)
print("Total Siblings:",length)

parents = ("Father", "Mother")

Family_Members = Siblings + parents
print("Family Members:",Family_Members)

#Level 2
Siblings = Family_Members[:4]
parents = Family_Members[4:]
print("Parents:",parents)
print("Siblings:",Siblings)

fruits = ("Mango", "Banana","Cherry")
vegetables = ("Tomato","Bringle","Spinach")
animal_product = ("Milk","Leather")

food_stuff_tp = fruits + vegetables + animal_product
print("food stuff:", food_stuff_tp)

food_stuff_list = list(food_stuff_tp)
print("Changed tuple to list:",food_stuff_list)

first_three_items = food_stuff_list[:3]
last_three_items = food_stuff_list[-3:]

print("First three items:", first_three_items)
print("Last three items:", last_three_items)


del food_stuff_tp

