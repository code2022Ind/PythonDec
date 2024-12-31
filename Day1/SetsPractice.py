

#Level 1


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 

length = len(it_companies)
print("1. the length of the set it_companies:", length)

it_companies.add("Twitter")
print("2.Add 'Twitter' to it_companies : ", it_companies)

it_companies.update(["TCS", "Wipro","Infosys","MUFG"])
print("3. Insert multiple IT companies at once to the set it_companies :",it_companies)

it_companies.remove("MUFG")
print("4.Remove one of the companies from the set it_companies:",it_companies)



#Level 2

A = {19, 22, 24, 20, 25, 26} 
B = {19, 22, 20, 25, 26, 24, 28, 27} 

union = A.union(B)
print("1. Join A and B :",union)

intersection_set = A.intersection(B)
print("2.Find A intersection B: ",intersection_set)

subset = A.issubset(B)
print("3.Is A subset of B : ",subset)

disjoint = A.isdisjoint(B)
print("4.Are A and B disjoint sets : ",disjoint)

JoinA = A.union(B)
JoinB = B.union(A)
print("5.Join A with B:",JoinA)
print("JoinB with A:",JoinB)

Symmetric_Diff =A.symmetric_difference(B)
print("6.the symmetric difference between A and B :",Symmetric_Diff)

del A
del B



#Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24] 

age_set = set(age)
length_set = len(age_set)
length_list = len(age)
print("1.Convert the ages to a set and compare the length of the list and the set",length_list)
print("Length of set: ",length_set)

if length_set > length_list :
    print("Set is greater")
else :
    print("List is bigger")

Scentence = "I am a teacher And I love to inspire and teach people."
split_sent = Scentence.split()
print("Split Sentence:",split_sent)

unique_word = set(Scentence)
print("Unique Words:",unique_word)

length = len(unique_word)
print("Length of unique words: ",length)