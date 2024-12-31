file = open("One.txt", "w")
file.close()
file1 = open("One.txt","r")
file1.close()
#file.write("XYZ")
print(file.readline()) # read line by line
print(file1.read()) # read entire file

# There are only three functions available in python for file handling
# w = write , r = read, a = append
#append is used to write in or to add in existing file
#write is used to write in file
#read = To read the data