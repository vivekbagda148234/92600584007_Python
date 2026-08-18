list=[11,22,33,44,55,66,77]

print("Indexing: ")
print("First Element= ",list[0])
print("Last Element= ",list[-1])

print("Slicing: ")
print("First 3 Elements=",list[:3])
print("Last 3 Elements=",list[-3:])
print("Revrese List=",list[::-1])

print("List Manipulation: ")
list.append(88)
print("After Append= ",list)
list.remove(22)
print("After Remove= ",list)

print("List Comprehension: ")
square=[x*x for x in list]
print("Sqaure List= ",square)
