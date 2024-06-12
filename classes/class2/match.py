name = input("State your name: ")

match name:
    case _ if name.startswith("S"):
        print("Starts with letter S")
    case _ if name.startswith("A"):
        print("Starts with letter A")
    case _ if name.startswith("C"):
        print("Starts with C")
    case _:
        print("Not yet specified. Try again later.")    