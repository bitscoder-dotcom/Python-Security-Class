
# Ask user to enter their name

name = input("Please enter your name: ").strip().title()

# Split user's name into first name and last name
firtsName, lastName = name.split(" ")

# print greeting

print(f"Welcome, {firtsName}")

