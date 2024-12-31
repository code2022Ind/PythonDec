Age = int(input("Enter your age:"))
print("Age",Age)

if Age > 18 :
    print("You are old enough to drive")
else:
    years_to_wait = 18 - Age
    print("wait for", years_to_wait, "the missing amount of years")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to 
# print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output: Enter your age: 30 You are 5 years older than me. 

my_age = 22
your_age = int(input("Enter Your Age:"))
if your_age > my_age:
    print("Youre older")

    difference = your_age - my_age
    if difference == 1:
        print("You are one year older than me")
    else:
        print("You are" {diffrence} "older than me")

elif my_age == your_age :
    print("Equal age")


