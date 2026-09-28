numbers = [1,2,3,4,5]
squares = [x * x for x in numbers]

print("List of numbers: ",numbers)
print("List of squares: ",squares)

squares_dict = {x: x * x for x in numbers}

print("Dictionary of sqaures: ", squares_dict)

even_set = {x for x in numbers if x % 2 == 0}

print("Set of even numbers: ", even_set)
