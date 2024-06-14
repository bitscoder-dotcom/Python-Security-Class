# edibles = {
#     "oranges" : "friuts",
#     "bread" : "carbohydrate",
#     "cherry" : "fruits",
#     "cucumber" : "vegetable",
#     "tomatoes" : "vegetable",
# }
# print(type(edibles))
# for edible in edibles:
#     print(edible, edibles[edible], sep=" belongs to class ")


edibles = [
    {"name" :"oranges", "class" : "friuts", "nutrient" : "vitamin"},
    {"name" : "bread", "class" : "carbohydrate", "nutrient" : "energy"},
    {"name" : "cherry", "class" : "fruits", "nutrient" : "vitamin"},
    {"name" : "cucumber", "class" : "vegetable", "nutrient" : "vitamins and fibre"},
    {"name" : "tomatoes", "class" : "vegetable", "nutrient" : "vitamins"}
]

print(type(edibles))
for edible in edibles:
    print(edible["name"], edible["class"], edible["nutrient"], sep=" | ")

    if edible.values == "vitamin":
        print(edible)

