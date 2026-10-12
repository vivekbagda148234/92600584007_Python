
import re

text = "Hello Python! My phone number is 999999999."


pattern1 = r"Python"
result1 = re.search(pattern1, text)

if result1:
    print("Word found:", result1.group())
else:
    print("Word not found.")


pattern2 = r"\d+"
result2 = re.findall(pattern2, text)
print("Numbers found:", result2)


pattern3 = r"^Hello"
result3 = re.match(pattern3, text)

if result3:
    print("Text starts with Hello.")
else:
    print("Text does not start with Hello.")


new_text = re.sub(r"Python", "AI", text)
print("Modified text:", new_text)
