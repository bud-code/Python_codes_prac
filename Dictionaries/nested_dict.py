students = {
        "student1": {
        "name": "Rahul",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "Amit",
        "age": 22,
        "marks": 90
    },

    "student3": {
        "name": "Priya",
        "age": 20,
        "marks": 95
    }
}


# Print complete dictionary
print(students)


# Access student1
print(students["student1"])


# Access specific value
print(students["student1"]["name"])
print(students["student2"]["marks"])


# Change value
students["student1"]["marks"] = 92
print(students)

# Add new value
students["student1"]["city"] = "Bangalore"
print(students)


# Loop through nested dictionary

for student_id, student_data in students.items():
    print("Student ID:", student_id)
    for key, value in student_data.items():
        print(key, ":", value)

    print()
