str1=input("Enter a String: ")

print("String Slicing: ")
print("Original String= ",str1)
print("First 3 Characters= ",str1[:3])
print("Last 3 Characters= ",str1[-3:])
print("Reverse String= ",str1[::-1])

print("String Formatting: ")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("My name is {} and I am {} years old".format(name,age))

print("Built-in String Functions: ")
print("Uppercase= ",str1.upper())
print("Lowercase= ",str1.lower())
print("Length= ",len(str1))
print("Replace= ",str1.replace("a","x"))
print("Count= ",str1.count("a"))      
