student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}


# get()
print(student.get("name"))
print(student.get("marks"))
print(student.get("marks", 0))

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# update()
student.update({
    "age": 22,
    "marks": 90
})

print(student)

# pop()
student.pop("age")
print(student)

# popitem()
student.popitem()
print(student)

# setdefault()
student.setdefault("city", "Bangalore")
print(student)


# copy()
new_student = student.copy()
print(new_student)


# clear()
new_student.clear()
print(new_student)
