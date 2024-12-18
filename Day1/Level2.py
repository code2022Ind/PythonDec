# Initial list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort ages and find min and max
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)

# Add min and max again to the list
#ages.extend([min_age, max_age])
ages = min_age + max_age
print("Ages after adding min and max again:", ages)

# Find median age
n = len(ages)
median = (ages[n//2 - 1] + ages[n//2]) / 2
 if n % 2 == 0 else ages[n//2]
print("Median age:", median)

# Find average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# Find range of ages
age_range = max_age - min_age
print("Age range:", age_range)

# Compare min - average and max - average
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min age difference from average:", min_diff)
print("Max age difference from average:", max_diff)

# Countries list
countries = ['China', 'Russia', 'USA', 'India', 'Sweden', 'Norway', 'Denmark']

# Find middle country(ies)
n_countries = len(countries)
middle_countries = [countries[(n_countries - 1) // 2]] 
