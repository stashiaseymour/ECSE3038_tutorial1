#Question 4
squares = [] 
even_numbers = []
upper_case_names = []

# a. Starting with an empty list, append the squares for the numbers from 1 to 5 using a for loop.
# b. Starting with an empty list, append the even numbers from 2 to 10 (inclusive) using a for loop.
# c. Using a for loop, create a list of names in uppercase from the list of people in Exercise 3.

squares = [] 
for i in range (1, 6):
    squares.append (i ** 2)
    print(squares)


even_numbers = []
for i in range (2,11,2):
    even_numbers.append(i)
    print(even_numbers)

people = [
    {"name": "Shelly", "age": 49, "city": "Port Maria"},
    {"name": "Eric", "age": 59, "city": "Border"},
    {"name": "Damion", "age": 35, "city": "Spanish Town"}
]

upper_case_names = []
for person in people:
    upper_case_names.append(person["name"].upper())
    print(upper_case_names)
