student = {
    "Name" : "Vivek",
    "Age" : 20,
    "Course" : "MCA",
    "Marks" : 95
    }

print("dictionary: ",student)

print("Keys: ",student.keys())
print("Values: ",student.values())
print("Items: ",student.items())
print("Name: ",student.get("Name"))

student["city"] = "Rajkot"
print("After adding city: ", student)

student["marks"] = 99
print("Afetr updating marks: ",student)

student.pop("Age")
print("After removing age: ",student)

print("\n Dictionary Elements: ")
for key, value in student.items():
    print(key,  ":", value)
