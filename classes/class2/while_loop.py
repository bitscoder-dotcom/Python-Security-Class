# I want the user to input only positive numbers

def main():
    number = get_number()
    loop_func(number)

def get_number():
    while True:
        num = int(input("What's your number? "))    
        if num > 0:
            break
    return num 

def loop_func(n):    
    for _ in range(n):
        print("in loop")    

main()        