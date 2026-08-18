def detail():
    print("Hello!")

def add(a, b):
    print("Addtion: ", a + b)

def welcome(name = "student"):
    print("Welcome", name)

def student(name, age):
    print("Name: ",name)
    print("Age: ",age)

def total(*numbers):
    print("Total: ", sum(numbers))


detail()

add(20, 9)

welcome()
welcome("Vivek")

student(age=20, name="Vivek")

total(20, 25, 30, 35, 40) 
