print("Break: ")
for i in range(1,6):
    if i == 4:
        break
    print(i)

print("Continue: ")
for i in range(1,6):
    if i == 3:
        continue
    print(i)

print("Pass")
for i in range(1,6):
    if i == 3:
        pass
    print(i)
