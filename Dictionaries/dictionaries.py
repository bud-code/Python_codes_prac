# Creating a dictionary

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print(student)


# Accessing values

print(student["name"])
print(student["age"])

# Using get()

print(student.get("course"))
print(student.get("city"))


# Adding a new key-value pair

student["city"] = "Bangalore"

print(student)


# Changing a value

student["marks"] = 90

print(student)


# Removing a key-value pair

student.pop("age")

print(student)


# Check if key exists

if "name" in student:
    print("Name exists")


# Length of dictionary

print(len(student))


# Keys

print(student.keys())


# Values

print(student.values())


# Key-value pairs

print(student.items())


# Copy dictionary

student2 = student.copy()

print(student2)


# Clear dictionary

student2.clear()

print(student2)
