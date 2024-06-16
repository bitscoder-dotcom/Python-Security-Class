with open("fruitList.csv") as file:
    for line in file:
        row = line.rstrip()
        print(row)