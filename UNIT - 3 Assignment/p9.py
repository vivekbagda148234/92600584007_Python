
import re

text = "Python is easy. Python is powerful. I love Python 777."


result1 = re.match("Python", text)
if result1:
    print("match():", result1.group())
else:
    print("No match found at the beginning.")


result2 = re.search("easy", text)
if result2:
    print("search():", result2.group())
else:
    print("No match found.")


result3 = re.findall("Python", text)
print("findall():", result3)


result4 = re.findall(r"\d+", text)
print("Digits:", result4)
