def main():
    # print_square(5)
    # print_square2(4)
    print_square3(4)

def print_square(size):
    # for each row
    for i in range(size):
        #  for each column in a row
        for j in range(size):
            print("[]", end="")
        print()

        # OR

def print_square2(size):
    for i in range(size):
        # using string multiplication instead
        print("[]" * size)

        # OR

def print_square3(size):
    for i in range(size):
        # using string multiplication instead
        print_width(size)

def print_width(width):
    print("[]" * width)

main()