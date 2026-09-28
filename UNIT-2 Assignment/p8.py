x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        y = 30

        print("Global variable: ",x)

        print("Nonlocal variable: ",y)

        z = 40
        print("Local variable: ",z)

    inner()

outer()
