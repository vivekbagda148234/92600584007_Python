
import re


with open("data.txt", "r") as file:
    text = file.read()


emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)


phones = re.findall(r'\b\d{10}\b', text)


numbers = re.findall(r'\b\d+\b', text)

print("Email Addresses:", emails)
print("Phone Numbers:", phones)
print("Numbers:", numbers)
