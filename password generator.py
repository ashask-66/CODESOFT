import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    character = random.choice(all_characters)
    password = password + character

print("Generated password:", password)

count_letters = 0
count_numbers = 0

for character in password:
    if character.isalpha():
        count_letters += 1
    elif character.isdigit():
        count_numbers += 1

print("Letters:", count_letters)
print("Numbers:", count_numbers)

print("Password created successfully")