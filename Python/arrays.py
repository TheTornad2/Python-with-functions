names = ["christopher", "Susan"]
print(len(names)) #get the number of items
#append(98) #Add new item to the end
names.insert(0, "Bill") # Insert before index
print(names)
 #Collections are Zero-Indexed

person = {"first": "Christopher"}
person ["last"] = "Harrison"
print(person)
print(person["first"])


#Normal loop , for every name in the array, print the name

for name in ["christopher", "Susan"]:
    print(name)


#To loop X number of times inside a list, we need to use the method range. this is going from 0 to 1

for index in range(0, 2):
    print(index)
    
# Looping with a condition

names = ["christopher", "Susan"]
index = 0  #Condition
while index < len(names):   #While index is less than the number of names
    print(names[index])     # Print all the names and their key
    #Change the condition
    Index = index + 1