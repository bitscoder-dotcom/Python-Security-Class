def main():
    num = int(input("Enter you digit:"))
    print(f"The {num} raised to power 2 = ", square(num))
    

def square(m):
    return pow(m, 2)


main()