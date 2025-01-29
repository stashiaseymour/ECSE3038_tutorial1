#Question 1
# Given the following dictionary representing a person:
person = {
    "name": "Alice",
    "age": 28,
    "city": "Wonderland"
}

# a. Print the person's name.
# b. Add a new key-value pair to represent the person's 
#    occupation (e.g., "engineer").
# c. Update the person's age to 29.
# d. Remove the "city" key from the dictionary.
# e. Print the keys of the modified dictionary.

print(person["name"])
person["occupation"] = "engineer"
person["age"] = 29
del person ["city"]
print("The updated dictionary keys are:", person.keys() )

