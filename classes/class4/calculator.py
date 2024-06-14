def main():
    number = int(input("What's your number? "))
    result = square(number)
    print(f"The square of {number} is:",result)


def square(num):
    squared = num * num

    return squared

if __name__ == "__main__":
    main()