edibles = [
    {"name": "oranges", "class": "friuts", "nutrient": "vitamin"},
    {"name": "bread", "class": "carbohydrate", "nutrient": "energy"},
    {"name": "cherry", "class": "fruits", "nutrient": "vitamin"},
    {"name": "cucumber", "class": "vegetable", "nutrient": "vitamins and fibre"},
    {"name": "tomatoes", "class": "vegetable", "nutrient": "vitamins"},
]

fruits = [fruit["name"] for fruit in edibles if fruit["class"] == "vegetable"]
"""
    using list comprehension to sort a list of dictionarys
"""

for edible in fruits:
    print(edible)
"""
    using for loop to print each individual output
"""

print()


def has_vitamin(food):
    return food["nutrient"] == "vitamin"


vitamins_foods = filter(has_vitamin, edibles)
"""
    :filter: using funtional approach to get desired result
"""

for food in vitamins_foods:
    print(food["name"])
