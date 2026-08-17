student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 90
}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through keys using keys()
for key in student.keys():
    print(key)

# Loop through key-value pairs
for key, value in student.items():
    print(key, ":", value)

# Check a particular key
for key in student:
    if key == "marks":
        print("Marks found")

# Print only numeric values
for key, value in student.items():
    if isinstance(value, int):
        print(key, value)
