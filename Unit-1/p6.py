print("TUPLE")
t = (10, 20, 30, 40, 50)

print("tuple: ",t)
print("First Element: ",t[0])
print("Last Element: ",t[-1])
print("Lenght of tuple: ",len(t))
print("Count of 20: ",t.count(20))
print("Index of 30: ",t.index(30))

print("\n SET")
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,100}

print("Set1: ",set1)
print("Set2: ",set2)

set1.add(29)
print("After adding 29 to Set1: ",set1)

set1.remove(30)
print("After removing 30 from Set1: ",set1)

print("Union: ", set1.union(set2))
print("Intersection: ", set1.intersection(set2))
print("Difference  (Set1 - Set2): ",set1.difference (set2))



