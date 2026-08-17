# Example 1

person = {
    "name": "John",
    "age": 25,
    "city": "Bangalore"
}

print(person["name"])


# Example 2 - Updating dictionary

person["age"] = 26

print(person)


# Example 3 - Adding data

person["job"] = "Developer"

print(person)


# Example 4 - Removing data

del person["city"]

print(person)


# Example 5 - Checking keys

if "job" in person:
    print("Job is present")


# Example 6 - Dictionary with different data types

data = {
    "name": "Alex",
    "age": 22,
    "marks": [80, 85, 90],
    "is_student": True
}

print(data)


# Example 7 - Dictionary as a phone book

phonebook = {
    "Rahul": "9876543210",
    "Amit": "9123456780",
    "John": "9988776655"
}

print(phonebook["Rahul"])


# Example 8 - Updating multiple values

phonebook.update({
    "Rahul": "1111111111",
    "Priya": "9999999999"
})

print(phonebook)
