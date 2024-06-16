name = (input("What's your name? "))

fruits = input("Please list the fruits you like separated by commas: ").split(",")

with open('fruitList', 'a') as fruit_list:
    if len(fruits) > 3:
        fruit_list.write(f"Wow!!! {name} you love a lot of fruits. \n")

    fruit_list.write(f"{name} likes: {', '.join(fruits)}\n")
    fruit_list.close()


