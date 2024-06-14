from calculator import square

def main():
    square_test_working()

def square_test_working():
    
    if square(9) != 81:
        print("Test failed: 9 squared was not 81")
    else:
        print("Test passed: 9 squared was 81")
    
    

if __name__ == "__main__":
    main()