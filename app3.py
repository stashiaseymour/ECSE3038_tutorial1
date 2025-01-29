#Question
# a. Create a list of dictionaries, where each dictionary represents a person.
people = [
    {"name": "Shelly", "age": 49, "city": "Port Maria"},
    {"name": "Eric", "age": 59, "city": "Border"},
    {"name": "Damion", "age": 35, "city": "Spanish Town"}
]

# b. Print the name of the second person in the list.
# c. Update the age of the third person to 30.
# d. Add a new person to the list.
# e. Print the list after the modifications.

print(people[1]["name"])
people[2]["age"]=30
new_person = {"name": "Tom", "age": 10, "city": "Half-Way-Tree"}
people.append(new_person)
print(people)