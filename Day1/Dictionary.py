a1 = {id:101, "name": "Python", "loc": "Bang"}
print(type(a1))
print(a1)
 
a1[id] =102
print(a1)

a1["Salary"] = 1000000
print(a1)

print(a1["loc"])

b1 = { 101:"Java",
    102:"Python",
    103:{"Python" : "Pandas",
          "Java": "Spring"}
}

print(b1[103] ["Python"])