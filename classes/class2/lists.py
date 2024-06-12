fruits = ["apple", "orange", "pineapple", "grape", "banana", "cherry"]

for fruit in fruits:
    if fruit.endswith("e"):
        print(fruit)

print()

"""
    range requires integer values
    to get the length in a list that has String, use len
"""

fruits = ["apple", "orange", "pineapple", "grape", "banana", "cherry"]

for i in range(len(fruits)):
    print(i +1, fruits[i])