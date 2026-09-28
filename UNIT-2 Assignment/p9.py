numbers = [10,20,30,40,50]

print("Iterable: ", numbers)

iterator = iter(numbers)

print("First element: ",next(iterator))
print("Second element: ",next(iterator))
print("Third element: ",next(iterator))
print("Fourth element: ",next(iterator))
print("Fifth element: ",next(iterator))
